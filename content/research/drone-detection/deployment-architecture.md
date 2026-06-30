---
title: "C-UAS Deployment Architecture for Fixed Critical Infrastructure"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Design pattern for building a counter-UAS detection system at a fixed critical infrastructure site: sensor placement geometry, integration architecture, power and networking, and maintenance cadence."
research_area: "drone-detection"
source_urls:
  - "https://www.criticalts.com/deployment-guides/counter-drone-detection-law-enforcement/"
  - "https://sentrycs.com/the-counter-drone-blog/securing-critical-infrastructure-with-integrated-counter-unmanned-aircraft-systems-c-uas/"
  - "https://www.defenseadvancement.com/feature/safeguarding-critical-infrastructure-against-rogue-drone-threats-with-c-uas-technology/"
  - "https://www.robinradar.com/blog/acoustic-sensors-drone-detection"
  - "https://www.crfs.com/blog/counter-drone-q-and-a"
  - "https://www.magaero.com/mag-thought-leadership-strategic-counter-uas-defense-technologies-and-mitigation-strategies/"
last_reviewed: 2026-06-05
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

A fixed-site C-UAS detection system is a layered architecture of complementary sensors, a fusion engine, alert workflow, and response protocol. This entry describes the design pattern for deploying such a system at a critical infrastructure site — a power substation, water treatment facility, data center, or government building — where the operator has legal authority to detect and track but not interdict (absent specific federal authorization).

## Key Facts

- **Type:** Design pattern
- **Applicable to:** Fixed critical infrastructure sites (commercial/non-federal operators)
- **Legal constraint:** Commercial operators may detect and track; RF jamming and cyber takeover are federally restricted — see [Regulatory Framework]({{< relref "regulatory-framework.md" >}})
- **Primary threat model:** RF-dark autonomous drones, fiber-optic FPV, consumer drones with RF control — see [Threat Taxonomy]({{< relref "threat-taxonomy.md" >}})
- **Minimum viable sensor set:** One micro-Doppler radar + RF receiver + one EO/IR camera for a small site

## Phase 1: Site Survey

Before procuring hardware, a site survey establishes the threat envelope and sensor placement geometry.

**Survey deliverables:**
- Site perimeter map with measured dimensions (or GIS shapefile)
- Elevation profile — buildings, terrain, and obstacles that create radar shadow zones
- RF noise floor measurement at candidate sensor locations (industrial RF noise from power equipment degrades RF detection)
- Acoustic noise baseline by location and time of day (generators, HVAC, road traffic all create false-positive pressure)
- Inventory of existing camera infrastructure that could be leveraged or integrated
- Identification of power and network availability at candidate sensor mounting points
- Local flight path data — nearby controlled airspace, helicopter corridors, bird migration routes that generate expected false positives

**Key output:** A coverage map with candidate sensor positions, expected detection range rings for each sensor type, and identified coverage gaps.

## Phase 2: Sensor Placement Geometry

### Micro-Doppler Radar

Radar is the primary sensor for most fixed-site deployments because it provides range, bearing, altitude, and micro-Doppler signature for drone-vs-bird discrimination regardless of RF silence or fiber-optic control. See [Micro-Doppler Radar]({{< relref "micro-doppler-radar.md" >}}).

**Coverage rules:**
- A single 360° radar node (e.g., Robin Radar IRIS, Fortem TrueView) covers roughly 1–3 km radius against small consumer-class drones depending on drone RCS and clutter environment.
- For rectangular sites, place radar at the highest available central point to maximize elevation coverage and minimize ground clutter.
- Identify radar shadow zones behind large buildings or embankments and cover them with secondary radar nodes or acoustic sensors.
- Overlapping radar coverage from two nodes is required if any shadow zone falls within the protected perimeter.
- Gap threshold: no unmonitored approach corridor should exceed 500 m for a high-value site.

### RF Detection

RF detection covers drones broadcasting Remote ID and those with active radio control links, but is blind to fiber-optic and pre-programmed autonomous threats. Useful as a secondary layer to corroborate radar tracks and gather operator-location data.

**Placement rules:**
- RF receivers (directional antenna arrays, omnidirectional sensors) require elevation above local RF noise sources (transformers, generators, motor drives).
- Minimum three receivers to enable TDOA (Time Difference of Arrival) triangulation for operator location.
- Spacing: receivers should be placed at least 50–100 m apart to achieve meaningful TDOA resolution; further separation improves triangulation accuracy.
- Avoid placing RF sensors on the same mounting structure as radar due to mutual interference.

### Acoustic Detection

Acoustic sensors detect propeller and motor noise. Effective range is typically 100–500 m in a low-noise environment; range collapses significantly in industrial noise environments (substations, water treatment plant aerators).

**Placement rules:**
- Acoustic sensors are most useful as a close-in perimeter layer, deployed inside the radar coverage footprint to provide positive confirmation when a radar track approaches the inner perimeter.
- Array configuration: a minimum of 4–5 microphone elements in a distributed array to enable direction-of-arrival estimation.
- Spacing within an array: 1–5 m element spacing for typical drone frequency range (50–8,000 Hz propeller harmonics).
- Inter-array spacing: arrays at 200–300 m intervals if acoustic is the primary close-in sensor.
- Avoid placement near HVAC exhausts, generators, or road edges.

### EO/IR Cameras

Electro-optical and IR cameras provide visual confirmation, record evidence, and enable classification by human operators or AI. IR cameras extend 24/7 capability beyond daylight hours.

**Placement rules:**
- Pan-tilt-zoom (PTZ) cameras with wide field of view are cueing targets, not primary detectors — they respond to radar or acoustic alerts.
- Fixed cameras require sufficient overlap (20–30% field-of-view overlap between adjacent cameras) to avoid coverage gaps at perimeter boundaries.
- IR cameras should be positioned to look toward the sky horizon, not down — downward angles increase ground clutter against elevated drone targets.
- Camera mounts on existing infrastructure (light poles, fence lines, rooftop parapets) reduce civil works cost.

## Phase 3: Integration Architecture

The sensor-to-alert-to-response chain follows a standard pipeline:

```
[Radar] ─┐
[RF]     ├──► [Sensor Fusion Engine] ──► [Operator Alert] ──► [Response Protocol]
[Acoustic]┤       (track correlation,      (priority queue,     (call authority,
[EO/IR]  ─┘        classification,          alert thresholds,    log evidence,
                    false-positive filter)   playbook trigger)    dispatch drone-dog)
```

**Fusion engine requirements:**
- Correlate tracks from multiple sensors into a unified air picture — a single drone should appear as one corroborated track, not four separate detections.
- Apply drone-vs-bird classification (micro-Doppler signature, flight path pattern, speed profile).
- Filter known airspace objects: authorized maintenance drones, adjacent airport traffic, recurring helicopter routes.
- Configurable alert thresholds by zone (outer detection zone: log; inner approach zone: alert; perimeter breach: alarm).
- Export to existing physical security systems (PSIM, VMS) via standard APIs (ATAK, REST, ONVIF).

**Networking:**
- Sensor-to-fusion: ethernet preferred; WiFi acceptable for camera feeds if encrypted (WPA3 minimum); cellular LTE/5G for remote or geographically distributed nodes.
- Bandwidth estimate: radar track stream ~1–5 Mbps; RF sensor data ~1 Mbps; compressed video ~4–8 Mbps per camera.
- Latency target: sensor-to-alert under 5 seconds from first radar detection to operator notification.
- Redundancy: UPS backup on fusion server and all sensor nodes; cellular failover for networking.

**Power:**
- Sensor mast power: standard 20A/120V circuit per mast is sufficient for most radar + RF + camera combos; add 30A/240V for heated enclosures in cold climates.
- Total system power draw (small site, 4–6 sensor nodes): 2–5 kW continuous.
- UPS runtime requirement: minimum 4 hours to maintain detection through grid interruption; site generators handle extended outages.

## Phase 4: Alert Workflow and Response Protocol

Detection capability alone does not protect a site. The alert workflow defines who receives alerts, what they do, and how the event is documented.

**Alert levels:**
1. **Detection:** Track confirmed, outside approach zone — log automatically, no human action required.
2. **Approach:** Track entering inner perimeter zone — notify duty security officer; begin recording.
3. **Intrusion:** Track within site boundary or overhead — alarm to all security staff; initiate response protocol; contact law enforcement.

**Response options for commercial operators:**
- Document and report to FAA (remote ID violations), local law enforcement, or FBI (critical infrastructure threats).
- Deploy counter-drone patrol drone (if DoD/DHS authorized) — otherwise observe only.
- Initiate lockdown or personnel shelter-in-place for high-value assets if threat classification escalates to potential armed drone.

**Evidence package:** The fusion engine should automatically generate a timestamped log of sensor detections, track replay, classification data, and video clips for law enforcement handoff.

## Phase 5: Maintenance Cadence

| Task | Frequency |
|------|-----------|
| Radar boresight verification and clutter map review | Monthly |
| RF receiver sensitivity check and frequency calibration | Monthly |
| Acoustic array microphone test and array sync check | Quarterly |
| Camera lens cleaning and PTZ range-of-motion test | Monthly |
| Fusion engine software update and signature library update | Per vendor release (monthly typical) |
| Full system operational test (inject test target, verify alert chain) | Quarterly |
| Site survey re-validation (new construction, changed RF environment) | Annually |
| False-positive / false-negative rate review | Quarterly |

## Deployment Scale Guidance

| Site Size | Minimum Sensor Set | Typical Node Count |
|-----------|-------------------|-------------------|
| Small (< 5 acres) | 1 radar, 2 RF receivers, 2 cameras | 3–4 nodes |
| Medium (5–50 acres) | 2 radar, 3–4 RF receivers, 4–6 cameras | 6–10 nodes |
| Large (50+ acres) | 3+ radar, 5+ RF receivers, 8+ cameras, acoustic arrays | 12–20+ nodes |

Large or complex sites (airports, large power generation facilities) typically engage a systems integrator to design the specific sensor geometry and tune the fusion engine.

## Related Entries

- [Micro-Doppler Radar]({{< relref "micro-doppler-radar.md" >}}) — primary detection modality
- [RF Detection]({{< relref "detection-methods/rf-detection.md" >}}) — Remote ID monitoring and protocol analysis
- [Acoustic Detection]({{< relref "acoustic-detection.md" >}}) — close-in perimeter layer
- [Multi-Sensor Fusion]({{< relref "detection-methods/multi-sensor-fusion.md" >}}) — fusion engine architecture
- [Regulatory Framework]({{< relref "regulatory-framework.md" >}}) — what commercial operators may legally do
- [Threat Taxonomy]({{< relref "threat-taxonomy.md" >}}) — threat types this architecture is designed against

## Sources

- [Counter-Drone Detection for Law Enforcement: Sensors, Masts, and Deployment Platforms](https://www.criticalts.com/deployment-guides/counter-drone-detection-law-enforcement/) — practical deployment guidance for fixed sites
- [Securing Critical Infrastructure with Integrated C-UAS](https://sentrycs.com/the-counter-drone-blog/securing-critical-infrastructure-with-integrated-counter-unmanned-aircraft-systems-c-uas/) — Sentrycs overview of layered C-UAS architecture
- [Safeguarding Critical Infrastructure Against Rogue Drone Threats](https://www.defenseadvancement.com/feature/safeguarding-critical-infrastructure-against-rogue-drone-threats-with-c-uas-technology/) — Defense Advancement feature on fixed-site deployment
- [Pros and Cons of Acoustic Detection](https://www.robinradar.com/blog/acoustic-sensors-drone-detection) — Robin Radar on acoustic placement and range limitations
- [Counter Drone System Q&A](https://www.crfs.com/blog/counter-drone-q-and-a) — CRFS on sensor integration and RF detection architecture
- [Strategic Counter-UAS Defense Technologies](https://www.magaero.com/mag-thought-leadership-strategic-counter-uas-defense-technologies-and-mitigation-strategies/) — MAG Aerospace on layered C-UAS strategy
