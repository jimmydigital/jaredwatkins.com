---
title: "EtherCAT Protocol Guide: Configuration and Communication"
date: 2026-06-26
lastmod: 2026-06-26
draft: false
description: "Protocol-level walkthrough of EtherCAT network startup, state machine transitions, CoE object dictionary, PDO mapping, SDO configuration, distributed clocks, and cyclic process data exchange for servo drives — with annotated C examples using SOEM."
tags: ["robotics", "ethercat", "fieldbus", "real-time", "motion-control", "servo", "SOEM", "CoE", "CiA402"]
categories: ["deep-dive"]
research_area: "robotics/ethercat"
last_reviewed: 2026-06-26
stale_after_days: 180
source_urls:
  - https://www.ethercat.org/en/technology.html
  - https://github.com/OpenEtherCATsociety/SOEM
  - https://doc.synapticon.com/actilink_s/system_integration/coe_cia_402.html
  - https://infosys.beckhoff.com/content/1033/ethercatsystem/1036980875.html
  - https://rt-labs.com/ethercat/implementing-distributed-clock-synchronization-in-ethercat-a-step-by-step-guide/
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Overview

This guide covers EtherCAT from the protocol layer up: how the network initializes, how the master communicates with slaves, how servo drives are configured using the CiA 402 profile, and how cyclic process data exchange works in practice. Code examples use [SOEM (Simple Open EtherCAT Master)](https://github.com/OpenEtherCATsociety/SOEM), the most widely used open-source EtherCAT master library, written in C and suitable for Linux, RTOS, and embedded targets.

This guide assumes you understand basic EtherCAT concepts (master/slave topology, on-the-fly processing). For protocol fundamentals see the [EtherCAT section overview]({{< relref "_index.md" >}}).

---

## The EtherCAT State Machine (ESM)

Every EtherCAT slave runs a state machine with four operational states. The master must walk each slave through these states in sequence at startup. You cannot skip states.

```
INIT → PRE-OP → SAFE-OP → OP
```

State transitions can go backward immediately (e.g., OP → INIT on fault), but forward transitions must be sequential.

### State Descriptions

| State | Mailbox | Process Data Inputs | Process Data Outputs | Typical Use |
|---|---|---|---|---|
| **INIT** | No | No | No | Reset, register access only |
| **PRE-OP** | Yes (CoE/SDO) | No | No | Configure PDO mapping, drive parameters |
| **SAFE-OP** | Yes | Yes (slave → master) | No (outputs safe/off) | Verify inputs before enabling outputs |
| **OP** | Yes | Yes | Yes | Normal operation — drives run |

### What Happens at Each Transition

**INIT → PRE-OP:** The master initializes the slave's mailbox (sync manager 0 and 1). The slave checks mailbox configuration. After this transition, CoE SDO communication is available — this is when you can read the object dictionary and configure PDO mapping.

**PRE-OP → SAFE-OP:** The master configures process data sync managers (SM2 for RxPDO, SM3 for TxPDO) based on the PDO mapping negotiated during PRE-OP. The slave begins populating TxPDO data (actual position, status). Slave outputs remain disabled — motors stay off.

**SAFE-OP → OP:** The master confirms it is sending valid RxPDO data. The slave enables outputs and begins processing RxPDO commands. **This is the moment drives become live.** From here, the cyclic process data loop controls the servo.

### SOEM: Driving the State Machine

SOEM provides `ec_writestate()` and `ec_statecheck()` for state control. The standard startup pattern:

```c
#include "ethercat.h"

#define EC_TIMEOUTMON 500
#define NSEC_PER_SEC  1000000000LL

int main(void) {
    /* Open NIC — use actual interface name: eth0, enp3s0, etc. */
    if (ec_init("eth0") <= 0) {
        fprintf(stderr, "ec_init() failed — check interface name and root privileges\n");
        return -1;
    }

    /* Enumerate all slaves on the bus. ec_config() puts slaves in PRE-OP. */
    int slave_count = ec_config(FALSE, &IOmap);
    if (slave_count <= 0) {
        fprintf(stderr, "No slaves found\n");
        ec_close();
        return -1;
    }
    printf("Found %d slaves\n", slave_count);

    /* Configure distributed clocks (see DC section below) */
    ec_configdc();

    /* Wait for all slaves to reach PRE-OP */
    ec_statecheck(0, EC_STATE_PRE_OP, EC_TIMEOUTSTATE * 4);

    /* ----- Configure slaves here via SDO (see CoE section) ----- */

    /* Request SAFE-OP */
    ec_slave[0].state = EC_STATE_SAFE_OP;
    ec_writestate(0);               /* 0 = broadcast to all slaves */
    ec_statecheck(0, EC_STATE_SAFE_OP, EC_TIMEOUTSTATE * 4);

    /* Verify actual state */
    ec_readstate();
    for (int i = 1; i <= ec_slavecount; i++) {
        printf("Slave %d: state=0x%04x, ALstatuscode=0x%04x, name=%s\n",
               i, ec_slave[i].state, ec_slave[i].ALstatuscode, ec_slave[i].name);
    }

    /* Request OP — from here the cyclic loop must run */
    ec_slave[0].state = EC_STATE_OPERATIONAL;
    ec_send_processdata();           /* Must send at least one cycle before OP */
    ec_writestate(0);
    ec_statecheck(0, EC_STATE_OPERATIONAL, EC_TIMEOUTSTATE * 4);

    /* ----- Start cyclic loop (see Process Data section) ----- */

    ec_close();
    return 0;
}
```

---

## CoE Object Dictionary

EtherCAT slave configuration uses **CANopen over EtherCAT (CoE)** — the same object dictionary structure as CANopen, transported over the EtherCAT mailbox channel rather than a CAN bus.

### Object Dictionary Structure

Every object has a **16-bit index** and up to 255 **8-bit sub-indices**. Objects are grouped into functional ranges:

| Index Range | Category | Examples |
|---|---|---|
| 0x0000–0x0FFF | Data types | — |
| 0x1000–0x1FFF | Communication parameters | Device type, identity, sync managers, PDO assignment |
| 0x2000–0x5FFF | Manufacturer-specific | Vendor-defined parameters |
| 0x6000–0x9FFF | Standardized profile objects | CiA 402 drive objects (position, velocity, torque, mode) |
| 0xA000–0xFFFF | Reserved | — |

### Key Standard Objects (0x1000–0x1FFF)

| Index | Name | Description |
|---|---|---|
| 0x1000 | Device Type | Lower word = device profile number (e.g., 0x0192 = CiA 402 drive) |
| 0x1008 | Manufacturer Device Name | ASCII string |
| 0x1018 | Identity Object | Sub-indices: 0=count, 1=VendorID, 2=ProductCode, 3=RevisionNumber, 4=SerialNumber |
| 0x1600–0x17FF | RxPDO Mapping | What objects are packed into each RxPDO (master→slave commands) |
| 0x1A00–0x1BFF | TxPDO Mapping | What objects are packed into each TxPDO (slave→master feedback) |
| 0x1C12 | SM2 PDO Assignment | Which RxPDO indices are assigned to sync manager 2 |
| 0x1C13 | SM3 PDO Assignment | Which TxPDO indices are assigned to sync manager 3 |

---

## Service Data Objects (SDO): Reading and Writing Configuration

SDOs use the mailbox channel (available in PRE-OP and above). They are used for **configuration-time** reads and writes — not real-time data. Think of SDOs as parameter access: you read the device identity, write operating mode, configure gains, set PDO mappings.

SOEM provides `ec_SDOread()` and `ec_SDOwrite()`:

```c
/* ---- Read device identity ---- */

uint32_t vendor_id = 0;
int size = sizeof(vendor_id);
/* ec_SDOread(slave_index, index, subindex, CA, psize, pdata, timeout_us) */
ec_SDOread(1, 0x1018, 0x01, FALSE, &size, &vendor_id, EC_TIMEOUTRXM);
printf("Slave 1 Vendor ID: 0x%08X\n", vendor_id);

uint32_t product_code = 0;
size = sizeof(product_code);
ec_SDOread(1, 0x1018, 0x02, FALSE, &size, &product_code, EC_TIMEOUTRXM);
printf("Slave 1 Product Code: 0x%08X\n", product_code);

/* ---- Write operating mode: Cyclic Synchronous Position (CSP = 8) ---- */
int8_t mode = 8;   /* CSP */
ec_SDOwrite(1, 0x6060, 0x00, FALSE, sizeof(mode), &mode, EC_TIMEOUTRXM);

/* ---- Read back to confirm ---- */
int8_t mode_display = 0;
size = sizeof(mode_display);
ec_SDOread(1, 0x6061, 0x00, FALSE, &size, &mode_display, EC_TIMEOUTRXM);
printf("Modes of Operation Display: %d\n", mode_display);

/* ---- Read actual position ---- */
int32_t actual_pos = 0;
size = sizeof(actual_pos);
ec_SDOread(1, 0x6064, 0x00, FALSE, &size, &actual_pos, EC_TIMEOUTRXM);
printf("Actual Position (encoder counts): %d\n", actual_pos);
```

SDO operations complete in one mailbox round-trip (typically 0.5–5 ms depending on cycle time and bus load). They must not be called from the real-time cyclic loop — they are configuration tools only.

---

## PDO Mapping: Configuring Real-Time Data

PDO mapping defines exactly what data travels in each real-time EtherCAT cycle. Each slave has:

- **RxPDO** (Receive PDO): Data the slave receives from the master — commands. Maps to output registers (target position, controlword, torque setpoint).
- **TxPDO** (Transmit PDO): Data the slave sends to the master — feedback. Maps to input registers (actual position, statusword, actual torque).

PDO mapping objects:
- **0x1600–0x17FF**: RxPDO mapping definitions
- **0x1A00–0x1BFF**: TxPDO mapping definitions
- **0x1C12**: SM2 assignment (which RxPDOs are active)
- **0x1C13**: SM3 assignment (which TxPDOs are active)

Each mapping entry encodes the object as `(index << 16) | (subindex << 8) | bit_length`. For example, the 16-bit Controlword at 0x6040:00 encodes as `0x60400010`.

### PDO Mapping Entry Encoding

```
Bits 31–16: Object index (e.g., 0x6040)
Bits 15–8:  Sub-index (e.g., 0x00)
Bits 7–0:   Bit length (e.g., 0x10 = 16 bits, 0x20 = 32 bits)
```

### Typical CiA 402 CSP PDO Layout

**RxPDO 0x1600 — Commands sent to the drive each cycle:**

| Sub-index | Object | Index:Sub | Bits | Description |
|---|---|---|---|---|
| 1 | Controlword | 0x6040:00 | 16 | Drive state command |
| 2 | Target Position | 0x607A:00 | 32 | Position setpoint (encoder counts) |
| 3 | Modes of Operation | 0x6060:00 | 8 | Operating mode (8=CSP, 9=CSV, 10=CST) |

Total RxPDO size: 16+32+8 = 56 bits = 7 bytes

**TxPDO 0x1A00 — Feedback received from the drive each cycle:**

| Sub-index | Object | Index:Sub | Bits | Description |
|---|---|---|---|---|
| 1 | Statusword | 0x6041:00 | 16 | Drive state feedback |
| 2 | Actual Position | 0x6064:00 | 32 | Encoder position (encoder counts) |
| 3 | Actual Velocity | 0x606C:00 | 32 | Actual velocity (units depend on drive) |

Total TxPDO size: 16+32+32 = 80 bits = 10 bytes

### Reconfiguring PDO Mapping via SDO (PRE-OP)

Some drives allow dynamic PDO remapping. The sequence is:

1. Disable PDO assignment (write 0 to 0x1C12:00 / 0x1C13:00)
2. Clear existing PDO mapping (write 0 to 0x1600:00 / 0x1A00:00)
3. Write new mapping entries (sub-indices 1..N of 0x1600 / 0x1A00)
4. Set entry count (write N to sub-index 0)
5. Re-assign PDO to sync manager (write PDO index back to 0x1C12:01 / 0x1C13:01)
6. Re-enable assignment (write 1 to 0x1C12:00 / 0x1C13:00)

```c
/* Reconfigure RxPDO mapping — must be in PRE-OP */
uint8_t  u8  = 0;
uint16_t u16 = 0;
uint32_t u32 = 0;

/* Step 1: Disable SM2 PDO assignment */
u8 = 0;
ec_SDOwrite(1, 0x1C12, 0x00, FALSE, sizeof(u8), &u8, EC_TIMEOUTRXM);

/* Step 2: Clear RxPDO 0x1600 mapping */
u8 = 0;
ec_SDOwrite(1, 0x1600, 0x00, FALSE, sizeof(u8), &u8, EC_TIMEOUTRXM);

/* Step 3: Map Controlword (0x6040, 16-bit) into entry 1 */
u32 = 0x60400010;
ec_SDOwrite(1, 0x1600, 0x01, FALSE, sizeof(u32), &u32, EC_TIMEOUTRXM);

/* Map Target Position (0x607A, 32-bit) into entry 2 */
u32 = 0x607A0020;
ec_SDOwrite(1, 0x1600, 0x02, FALSE, sizeof(u32), &u32, EC_TIMEOUTRXM);

/* Map Modes of Operation (0x6060, 8-bit) into entry 3 */
u32 = 0x60600008;
ec_SDOwrite(1, 0x1600, 0x03, FALSE, sizeof(u32), &u32, EC_TIMEOUTRXM);

/* Step 4: Set entry count to 3 */
u8 = 3;
ec_SDOwrite(1, 0x1600, 0x00, FALSE, sizeof(u8), &u8, EC_TIMEOUTRXM);

/* Step 5: Assign 0x1600 to SM2 */
u16 = 0x1600;
ec_SDOwrite(1, 0x1C12, 0x01, FALSE, sizeof(u16), &u16, EC_TIMEOUTRXM);

/* Step 6: Enable SM2 with 1 PDO */
u8 = 1;
ec_SDOwrite(1, 0x1C12, 0x00, FALSE, sizeof(u8), &u8, EC_TIMEOUTRXM);
```

Many commercial drives have fixed default PDO mappings that match the above and do not require remapping — check the drive manual. Reconfiguration is needed when adding objects like target velocity feed-forward or digital I/O to the cyclic data.

---

## CiA 402 Drive Profile: Enabling a Servo

The CiA 402 profile (IEC 61800-7) defines a standard state machine and object dictionary for servo drives. It is used by virtually all EtherCAT servo drives — Beckhoff, Yaskawa, Panasonic, Synapticon, Kollmorgen, Elmo, Maxon, etc. Understanding CiA 402 is prerequisite to commanding any of them.

### CiA 402 State Machine

The drive has its own state machine, controlled via **Controlword (0x6040)** and reflected in **Statusword (0x6041)**. This is separate from the EtherCAT ESM — even when EtherCAT is in OP, the drive starts in its own disabled state.

```
Not Ready to Switch On
        ↓
Switch On Disabled   ← automatic on power-up
        ↓ (Shutdown command)
Ready to Switch On
        ↓ (Switch On command)
Switched On
        ↓ (Enable Operation command)
Operation Enabled    ← motor is live, setpoints active
        ↓
Quick Stop Active  (on QS command or fault)
        ↓
Fault Reaction Active
        ↓
Fault              ← requires Fault Reset command
```

### Controlword Commands (0x6040)

| Command | Controlword Value | Transition |
|---|---|---|
| Shutdown | 0x0006 | Switch On Disabled → Ready to Switch On |
| Switch On | 0x0007 | Ready to Switch On → Switched On |
| Enable Operation | 0x000F | Switched On → Operation Enabled |
| Disable Voltage | 0x0000 | Any → Switch On Disabled |
| Quick Stop | 0x0002 | Any → Quick Stop Active |
| Fault Reset | 0x0080 (rising edge) | Fault → Switch On Disabled |

### Statusword Masks (0x6041)

| Bits | Mask | State |
|---|---|---|
| 3:0 | 0x004F | Not Ready = 0x0000 |
| 3:0 | 0x004F | Switch On Disabled = 0x0040 |
| 3:0 | 0x006F | Ready to Switch On = 0x0021 |
| 3:0 | 0x006F | Switched On = 0x0023 |
| 3:0 | 0x006F | Operation Enabled = 0x0027 |
| 3:0 | 0x006F | Quick Stop Active = 0x0007 |
| 3:0 | 0x004F | Fault Reaction = 0x000F |
| 3:0 | 0x004F | Fault = 0x0008 |

Bit 3 (Fault) and bit 5 (Quick Stop) and bit 6 (Switch On Disabled) are the most useful for state decoding.

### Modes of Operation (0x6060)

| Value | Mode | Description |
|---|---|---|
| 1 | PP — Profile Position | Master sends target position; drive executes point-to-point with internal ramp |
| 3 | PV — Profile Velocity | Master sends target velocity; drive ramps to it |
| 4 | PT — Profile Torque | Master sends target torque |
| 6 | HM — Homing | Drive executes a homing sequence |
| 8 | CSP — Cyclic Synchronous Position | Master streams position every cycle; drive closes position loop |
| 9 | CSV — Cyclic Synchronous Velocity | Master streams velocity every cycle; drive closes velocity loop |
| 10 | CST — Cyclic Synchronous Torque | Master streams torque every cycle; drive closes torque loop |

CSP, CSV, and CST are the preferred modes for real-time EtherCAT control because they let the master controller run the outer loop. PP/PV/PT execute profiles internally and are less suited to tightly synchronized multi-axis motion.

---

## Process Data Exchange: The Cyclic Loop

Once in OP, the master runs a fixed-rate cyclic loop. Every cycle: send a frame with all slave RxPDO data, receive the frame with all slave TxPDO data. The entire round-trip is one EtherCAT frame — regardless of how many slaves are on the bus.

### Process Data Map (IOmap)

SOEM builds a contiguous byte array (`IOmap`) that holds all slaves' process data. After `ec_config()`, each slave's input and output pointers are set:

- `ec_slave[i].outputs` — pointer into IOmap at the slave's RxPDO offset
- `ec_slave[i].inputs` — pointer into IOmap at the slave's TxPDO offset

You cast these pointers to your drive-specific struct to read/write process data directly.

### Struct Definitions for CiA 402 CSP

```c
#pragma pack(1)  /* Ensure no padding between struct members */

/* RxPDO: sent to drive each cycle (7 bytes for the mapping above) */
typedef struct {
    uint16_t controlword;      /* 0x6040 — drive state command       */
    int32_t  target_position;  /* 0x607A — position setpoint (counts) */
    int8_t   mode_of_op;       /* 0x6060 — 8=CSP, 9=CSV, 10=CST      */
} rxpdo_t;

/* TxPDO: received from drive each cycle (10 bytes for the mapping above) */
typedef struct {
    uint16_t statusword;        /* 0x6041 — drive state feedback      */
    int32_t  actual_position;   /* 0x6064 — encoder position (counts) */
    int32_t  actual_velocity;   /* 0x606C — actual velocity           */
} txpdo_t;

#pragma pack()
```

### The Real-Time Cyclic Loop

```c
#include <time.h>
#include "ethercat.h"

#define CYCLE_NS   1000000LL   /* 1 ms cycle time */

static char IOmap[4096];

/* Helper: add nanoseconds to a timespec */
static void timespec_add_ns(struct timespec *ts, long ns) {
    ts->tv_nsec += ns;
    while (ts->tv_nsec >= 1000000000LL) {
        ts->tv_nsec -= 1000000000LL;
        ts->tv_sec++;
    }
}

void cyclic_loop(int slave_idx) {
    rxpdo_t *out = (rxpdo_t *)ec_slave[slave_idx].outputs;
    txpdo_t *in  = (txpdo_t *)ec_slave[slave_idx].inputs;

    /* Initialize RxPDO to safe defaults */
    out->controlword     = 0x0000;  /* Disable voltage */
    out->target_position = 0;
    out->mode_of_op      = 8;       /* CSP */

    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);

    int state = 0;  /* Simple enable sequencer state */

    while (1) {
        /* 1. Send process data frame to all slaves */
        ec_send_processdata();

        /* 2. Wait for return frame (timeout in µs) */
        ec_receive_processdata(EC_TIMEOUTRET);

        /* ---- Read slave feedback ---- */
        uint16_t sw  = in->statusword;
        int32_t  pos = in->actual_position;

        /* ---- CiA 402 enable sequence ---- */
        switch (state) {
            case 0:
                /* Step 1: Send Shutdown to reach Ready to Switch On */
                out->controlword = 0x0006;
                if ((sw & 0x006F) == 0x0021) state = 1;  /* Ready to Switch On */
                break;
            case 1:
                /* Step 2: Send Switch On */
                out->controlword = 0x0007;
                if ((sw & 0x006F) == 0x0023) state = 2;  /* Switched On */
                break;
            case 2:
                /* Step 3: Enable Operation */
                out->controlword = 0x000F;
                if ((sw & 0x006F) == 0x0027) {
                    /* Capture current position as initial setpoint */
                    out->target_position = pos;
                    state = 3;  /* Operation Enabled */
                }
                break;
            case 3:
                /* Drive is live — update target from your trajectory generator */
                out->target_position = get_trajectory_setpoint();  /* your function */
                out->controlword     = 0x000F;

                /* Check for fault */
                if (sw & 0x0008) {
                    fprintf(stderr, "Drive fault! SW=0x%04X\n", sw);
                    out->controlword = 0x0080;  /* Fault reset rising edge */
                    state = 4;
                }
                break;
            case 4:
                out->controlword = 0x000F;  /* Clear fault reset bit */
                state = 0;                  /* Re-run enable sequence */
                break;
        }

        /* ---- Deadline sleep for next cycle ---- */
        timespec_add_ns(&ts, CYCLE_NS);
        clock_nanosleep(CLOCK_MONOTONIC, TIMER_ABSTIME, &ts, NULL);
    }
}
```

Key points:
- `ec_send_processdata()` / `ec_receive_processdata()` are the only two EtherCAT calls in the hot path
- The enable sequence (state 0→3) is driven cycle by cycle, not with sleep loops
- `target_position` must be updated every cycle in CSP mode — the drive expects a fresh setpoint
- Never call SDO functions from this loop — they use the mailbox and block

---

## Distributed Clocks (DC): Multi-Axis Synchronization

Without distributed clocks, each drive uses its own local oscillator. Even with identical cycle times, drives execute their control loops at slightly different moments — introducing inter-axis synchronization error that grows with the number of joints.

Distributed clocks solve this by hardware-synchronizing all slave local clocks to a single reference (typically the first slave with DC capability). The master calls `ec_configdc()` after `ec_config()`. SOEM automatically:

1. Identifies the DC reference slave (first DC-capable slave found)
2. Measures propagation delay to each slave and stores offsets
3. Writes each slave's system time offset so local clocks report the same time as the reference
4. Configures SYNC0 events on each slave — periodic hardware interrupts that trigger the drive's control loop at a deterministic wall-clock time

### SYNC0 Configuration

SYNC0 is the interrupt that tells the drive "now is the start of your control cycle." When DC is active, every slave fires SYNC0 at the same absolute time (modulo propagation delay correction). This is what achieves <1 µs inter-axis jitter.

```c
/*
 * ec_configdc() handles reference clock selection and delay measurement.
 * After calling it, per-slave DC can be tuned:
 */

/* Set SYNC0 cycle time (ns) and start offset (ns) for slave 1 */
/* ec_dcsync0(slave, active, cycle_time_ns, cycleshift_ns) */
ec_dcsync0(1, TRUE, CYCLE_NS, 0);

/*
 * For SYNC1 (used for secondary timing, e.g., triggering ADC reads
 * at mid-cycle for better latency):
 */
ec_dcsync01(1, TRUE, CYCLE_NS, CYCLE_NS / 2, 0);
```

After configuring DC, the master should synchronize its own send timing to the DC reference. The standard approach (RT-Linux): read the reference slave's system time register (`0x0910`) and phase-lock the `clock_nanosleep` wakeup to the DC epoch.

```c
/* Read DC reference time from slave 1 (or whichever is DC ref) */
uint64_t dc_time = 0;
int size = sizeof(dc_time);
ec_SDOread(1, 0x0910, 0x00, FALSE, &size, &dc_time, EC_TIMEOUTRXM);
/* Use dc_time to align your cyclic wakeup to the DC epoch */
```

In practice, most SOEM-based systems use a separate DC synchronization thread that reads `ec_DCtime` (the master-side DC time estimate) and adjusts the cyclic thread's period using a PI controller — the same technique used by LinuxCNC's EtherCAT driver.

### DC Topology Note

In a line topology, propagation delay increases with distance. SOEM measures the round-trip delay and computes the per-slave offset automatically. For ring topologies (cable redundancy), the reference is still the first DC-capable slave; the redundant path is used for fault recovery, not for timing.

---

## Multi-Slave Example: Three-Axis Robot

For a 3-axis robot with one EtherCAT servo per joint:

```c
#pragma pack(1)
typedef struct { uint16_t cw; int32_t tgt_pos; int8_t mode; } rxpdo_t;
typedef struct { uint16_t sw; int32_t act_pos; int32_t act_vel; } txpdo_t;
#pragma pack()

static char IOmap[4096];

void robot_cyclic_loop(void) {
    /* SOEM places slaves in order of physical position on the bus */
    rxpdo_t *axis[4];  /* index 1..3 */
    txpdo_t *fdbk[4];

    for (int i = 1; i <= ec_slavecount; i++) {
        axis[i] = (rxpdo_t *)ec_slave[i].outputs;
        fdbk[i] = (txpdo_t *)ec_slave[i].inputs;
        axis[i]->mode = 8;  /* CSP for all axes */
    }

    while (1) {
        ec_send_processdata();
        ec_receive_processdata(EC_TIMEOUTRET);

        /* Read all feedback atomically (one network cycle) */
        for (int i = 1; i <= ec_slavecount; i++) {
            printf("Axis %d: sw=0x%04X pos=%d vel=%d\n",
                   i, fdbk[i]->statusword,
                   fdbk[i]->actual_position,
                   fdbk[i]->actual_velocity);
        }

        /* Write all setpoints — all transmitted in same frame */
        axis[1]->target_position = joint1_setpoint;
        axis[2]->target_position = joint2_setpoint;
        axis[3]->target_position = joint3_setpoint;

        /* All three drives receive their setpoints in the same
           EtherCAT frame and execute them at the same SYNC0 event.
           This is the key advantage over CAN: true simultaneous
           multi-axis setpoint delivery. */

        nanosleep_until_next_cycle();
    }
}
```

All three axes receive their new setpoints in one Ethernet frame and latch them at the same SYNC0 hardware interrupt. On CAN, you would send three separate messages with non-zero inter-message latency.

---

## Reading Non-Servo Devices: Digital I/O and Analog Modules

EtherCAT is not just for servo drives. I/O modules (Beckhoff EL series, Phoenix Contact Axioline, etc.) use the same protocol with simpler PDO layouts.

### Digital I/O Module Example

A Beckhoff EL2008 (8-channel digital output) or EL1008 (8-channel digital input) maps its entire state into a single byte in the process image:

```c
/* Digital output module — 8 outputs packed in 1 byte */
typedef struct {
    uint8_t outputs;   /* bit 0 = channel 1, bit 7 = channel 8 */
} dio_out_t;

/* Digital input module — 8 inputs packed in 1 byte */
typedef struct {
    uint8_t inputs;
} dio_in_t;

/* Assuming slave 2 is a DIO output module */
dio_out_t *dio = (dio_out_t *)ec_slave[2].outputs;

/* Set channels 1 and 3 high, rest low */
dio->outputs = 0b00000101;
```

### Analog Input Module Example

A Beckhoff EL3104 (4-channel ±10V analog input, 16-bit) maps each channel as a signed 16-bit integer:

```c
#pragma pack(1)
typedef struct {
    int16_t ch1;   /* Raw ADC value: -32768 to +32767 = -10V to +10V */
    int16_t ch2;
    int16_t ch3;
    int16_t ch4;
} analog_in_t;
#pragma pack()

analog_in_t *ain = (analog_in_t *)ec_slave[3].inputs;

/* Convert to voltage: value / 32768.0 * 10.0 */
float voltage_ch1 = ain->ch1 / 32768.0f * 10.0f;
```

All devices — servo drives, I/O modules, analog modules, encoders — appear as consecutive segments in the IOmap. The master writes and reads all of them in one frame per cycle, with no additional overhead per device type.

---

## ENI Files: Pre-Configured Networks

For production deployments, EtherCAT network configuration is typically stored in an **ENI file** (EtherCAT Network Information, XML format), generated by a configuration tool (Beckhoff TwinCAT, Omron Sysmac Studio, or open-source tools like `ec-configuration`).

An ENI file contains:
- Full slave enumeration with vendor/product IDs
- PDO mapping configuration
- DC settings per slave
- SDO initialization commands to run at startup
- Process data offsets

SOEM 2.0 introduced an ENI parser that reads the XML and generates a C initialization file, eliminating manual SDO startup sequence coding. This is the recommended approach for production systems with fixed hardware configurations.

---

## Debugging and Diagnostics

### AL Status Code

When a slave fails to reach a requested state, `ec_slave[i].ALstatuscode` contains the reason:

| Code | Meaning |
|---|---|
| 0x0000 | No error |
| 0x001B | Sync manager watchdog — master stopped sending frames |
| 0x001D | Invalid SM configuration |
| 0x0025 | PDO size mismatch |
| 0x002B | DC sync error |

Read it after a failed state transition: `printf("AL status: 0x%04X\n", ec_slave[i].ALstatuscode);`

### Working Counter

Every EtherCAT frame returns a **working counter** — the number of slaves that successfully processed the frame. If `ec_receive_processdata()` returns fewer than expected, a slave missed the frame:

```c
int wkc = ec_receive_processdata(EC_TIMEOUTRET);
int expected_wkc = (ec_group[0].outputsWKC * 2) + ec_group[0].inputsWKC;
if (wkc < expected_wkc) {
    fprintf(stderr, "WKC error: got %d expected %d\n", wkc, expected_wkc);
    /* Trigger recovery: check slave states, re-attempt OP */
}
```

Working counter errors indicate cable faults, EMI, or a slave that has left OP due to watchdog timeout.

### EtherCAT Slave Information (ESI) Files

Every conformant slave ships with an ESI file (XML, `.xml`), which describes the device's object dictionary, PDO options, and default configuration. ESI files are the authoritative source for what objects a device supports. They are imported into configuration tools (TwinCAT, Sysmac) and can be read manually to determine valid PDO mapping options and SDO parameter ranges.

---

## Reference

- [SOEM GitHub](https://github.com/OpenEtherCATsociety/SOEM) — Source, `simple_test.c` example, issue tracker
- [ETG EtherCAT Technology Overview](https://www.ethercat.org/en/technology.html) — Official specification summary
- [Synapticon CiA 402 / CoE Documentation](https://doc.synapticon.com/actilink_s/system_integration/coe_cia_402.html) — Detailed CiA 402 object reference with examples
- [Beckhoff EtherCAT System Documentation](https://infosys.beckhoff.com/content/1033/ethercatsystem/1036980875.html) — ESM state machine reference
- [RT-Labs: Implementing Distributed Clock Synchronization](https://rt-labs.com/ethercat/implementing-distributed-clock-synchronization-in-ethercat-a-step-by-step-guide/) — Step-by-step DC guide
- [acontis: CoE / Mailbox API](https://public.acontis.com/manuals/EC-Master/3.1/html/ec-master-class-b/mbx_coe.html) — Commercial master API reference; useful for SDO patterns
- [ETG.6010 CiA 402 Implementation Directive](https://www.ethercat.org/etg6010/) — Official interoperability requirements for CiA 402 over EtherCAT
