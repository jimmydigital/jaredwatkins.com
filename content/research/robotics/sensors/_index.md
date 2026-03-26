---
title: Robotics Sensors
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: LiDAR, radar, IMUs, GNSS, cameras, and force/torque sensors for robot perception — manufacturers, technology trends, and supply chain.
tags: ["robotics", "sensor", "lidar", "gnss", "radar"]
categories: ["overview"]
research_area: "robotics/sensors"
last_reviewed: 2026-03-24
stale_after_days: 90
---

## Overview

Sensors are the eyes and proprioception of robots. The robotics sensor landscape is undergoing rapid commoditization driven primarily by Chinese LiDAR manufacturers (Hesai, RoboSense) whose price points are compressing the market faster than US and Israeli competitors can respond. At the same time, the GNSS and IMU layers are dominated by near-monopoly suppliers (u-blox for civil GNSS modules, InvenSense/TDK and Bosch for MEMS IMUs) that represent shared infrastructure risk across almost every robot platform. Force/torque sensing — critical for manipulation and human-robot collaboration — is a smaller, more defensible niche.

## Key Themes

- LiDAR commoditization: Hesai and RoboSense offering >90% of Ouster/Velodyne performance at 40–60% lower price
- u-blox near-monopoly in civil GNSS modules across virtually all non-defense robot platforms
- MEMS IMU supply concentrated in three companies (InvenSense/TDK, Bosch Sensortec, STMicroelectronics)
- Thermal imaging: Teledyne FLIR dominant, US export controlled — creates a non-tariff barrier to Chinese drone/robot makers
- Solid-state LiDAR transition: MEMS-based designs (Innoviz, Cepton/Koito) vs. spinning designs — automotive pull driving investment
- Depth cameras: Intel RealSense retreat creating a gap that Stereolabs ZED and Luxonis OAK-D are filling

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Ouster](https://ouster.com) | San Francisco, CA, USA | Public (NYSE: OUST) | Digital spinning LiDAR (OS series); formed by merger with Velodyne 2023; broad robotics, AV, and industrial market. |
| [Innoviz Technologies](https://innoviz.tech) | Rosh HaAyin, Israel | Public (NASDAQ: INVZ) | MEMS solid-state LiDAR (InnovizOne, InnovizTwo); BMW OEM design win; targets automotive-grade qualification. |
| [Stereolabs](https://www.stereolabs.com) | Paris, France / San Francisco, CA | Series B | ZED stereo camera series (active stereo vision); popular in AMR, drone, and research robotics; NVIDIA partnership for Jetson integration. |
| [Luxonis](https://luxonis.com) | Denver, CO, USA | Series A | OAK-D spatial AI camera (depth + neural inference on-device); popular in research and development-stage robots. |
| [LightWare](https://lightwarelidar.com) | Johannesburg, South Africa | Growth | Compact micro-LiDAR for drone altitude hold and obstacle avoidance; SF and LW series; widely specified into professional drone platforms. |
| [Robosense](https://www.robosense.ai) 🇨🇳 | Shenzhen, China | Public (HKEX: 2498) | Spinning and solid-state LiDAR; competitive pricing with Hesai; strong China AMR and automotive market. |
| [Hesai Technology](https://www.hesaitech.com) 🇨🇳 | Shanghai, China | Public (NASDAQ: HSAI) | AT128, XT32, QT128 spinning LiDAR and solid-state variants; aggressive pricing; growing international AMR and AV share. |
| [Cepton](https://www.cepton.com) | San Jose, CA, USA | Acquired (Koito Mfg., Japan) | MEMS-based solid-state LiDAR; acquired by Koito Manufacturing (Japan, major Tier-1 auto supplier) 2023. |
| [WayRay](https://wayray.com) | Zurich, Switzerland | Series C | Holographic AR displays and sensing; sensor-adjacent technology. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [OUST](https://finance.yahoo.com/quote/OUST) | [Ouster](https://ouster.com) | Post-merger LiDAR company (Velodyne + Ouster); serving robotics, AV, industrial, and smart infrastructure. |
| [LAZR](https://finance.yahoo.com/quote/LAZR) | [Luminar Technologies](https://luminartech.com) | Automotive-grade Iris and Halo LiDAR; Volvo, Mercedes OEM wins; time-of-flight with 1550nm laser for long range. |
| [INVZ](https://finance.yahoo.com/quote/INVZ) | [Innoviz Technologies](https://innoviz.tech) | Israeli MEMS solid-state LiDAR; BMW design win; automotive-grade qualification path. |
| [HSAI](https://finance.yahoo.com/quote/HSAI) | [Hesai Technology](https://www.hesaitech.com) 🇨🇳 | Chinese LiDAR manufacturer listed on Nasdaq; dominant in mid-market robotics and AV globally by volume. |

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "Sensors",
        "symbols": [
          {"s": "NYSE:OUST", "d": "Ouster"},
          {"s": "NASDAQ:LAZR", "d": "Luminar Technologies"},
          {"s": "NASDAQ:INVZ", "d": "Innoviz Technologies"},
          {"s": "NASDAQ:HSAI", "d": "Hesai Technology"}
        ],
        "originalTitle": "Sensors"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [TDK](https://finance.yahoo.com/quote/TTDKF) | [TDK / InvenSense](https://invensense.tdk.com) | Dominant MEMS IMU supplier (ICM series); acquired InvenSense 2017; IMUs appear in virtually every drone and mobile robot. |
| [UBXN.SW](https://finance.yahoo.com/quote/UBXN.SW) | [u-blox](https://www.u-blox.com) | Near-monopoly civil GNSS module supplier; M8, M9, F9 series used in drones, AMRs, agricultural robots, and delivery platforms globally. |
| [TDY](https://finance.yahoo.com/quote/TDY) | [Teledyne Technologies](https://www.teledyne.com) | Parent of Teledyne FLIR; Boson and Lepton thermal camera modules used across drones, UGVs, and security robots; US export controlled. |
| [STM](https://finance.yahoo.com/quote/STM) | [STMicroelectronics](https://www.st.com) | IMU, gyroscope, accelerometer (LSM, ISM series); major MEMS sensor supplier alongside TDK/InvenSense and Bosch. |
| [HESM](https://finance.yahoo.com/quote/HESM) | [Hexagon AB](https://hexagon.com) | NovAtel (RTK GNSS), Leica Geosystems; survey-grade and precision RTK receivers for agricultural and survey robots. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Raw Materials** | Silicon wafers (MEMS), indium phosphide / gallium arsenide (laser diodes), glass (optics), rare earths (some laser materials) | Shin-Etsu (Japan, silicon wafers), Sumitomo Electric (Japan, InP), II-VI / Coherent (US, compound semiconductors) | Silicon wafer: Japan dominant (Shin-Etsu, Sumco); compound semiconductor: US and Japan |
| **2. Core Sensing Elements** | MEMS accelerometers/gyros (IMU), photodetectors (LiDAR), CMOS image sensors, laser diodes | InvenSense/TDK (MEMS), Bosch Sensortec (MEMS), Sony (CMOS, STARVIS series), Ams-OSRAM (laser diodes), II-VI/Coherent (905nm/1550nm lasers) | CMOS image sensors: Sony dominant (~50% global CMOS market); MEMS: Japan, US, and Germany; laser diodes: US and Germany |
| **3. Sensor Modules** | IMU modules, GNSS receiver modules, thermal camera cores, depth camera units | [u-blox](https://www.u-blox.com) (GNSS), [InvenSense/TDK](https://invensense.tdk.com) (IMU), [Teledyne FLIR](https://www.flir.com) (thermal cores), [Bosch Sensortec](https://www.bosch-sensortec.com) (IMU) | GNSS modules: u-blox near-monopoly in civil market; thermal: FLIR US-controlled |
| **4. Complete Sensor Systems** | Full LiDAR units, RTK GNSS systems, force/torque sensors | [Ouster](https://ouster.com) (US), [Luminar](https://luminartech.com) (US), [Hesai](https://www.hesaitech.com) 🇨🇳, [RoboSense](https://www.robosense.ai) 🇨🇳, [ATI Industrial Automation](https://www.ati-ia.com) (force/torque), [NovAtel/Hexagon](https://novatel.com) (RTK) | LiDAR system assembly: Chinese manufacturers taking volume share; force/torque: US niche |
| **5. Integration into Robot Platforms** | Sensor-fused perception stacks, SLAM pipelines | Robot OEMs, Tier-1 integrators; NVIDIA (Jetson + Isaac ROS ecosystem) | Software and integration: US and Europe dominant; hardware: mixed |

### Key Supply Chain Notes

**⚑ Shared supplier — u-blox:** u-blox GNSS modules appear in DJI consumer drones, Skydio X10, Parrot ANAFI, AeroVironment Puma, Starship delivery robots, Monarch tractors, John Deere guidance systems, and virtually every precision mobile robot not using a proprietary GNSS solution. This is the highest-concentration single-supplier risk in the entire robotics sensor stack. u-blox is a small Swiss public company (~2,000 employees) — its manufacturing is outsourced to Asian contract manufacturers, adding a secondary geographic risk.

**⚑ Shared supplier — Sony CMOS sensors:** Sony's IMX series image sensors are the dominant visible-light sensor in drone cameras (DJI uses Sony sensors), AMR cameras, and general machine vision. Sony's Kumamoto, Japan sensor fab was affected by the 2016 earthquake, highlighting the geographic concentration risk. Sony controls approximately 50% of the global CMOS image sensor market.

**LiDAR pricing compression:** Hesai's AT128 (128-channel spinning LiDAR) is priced at approximately $800–1,200 in volume versus comparable Ouster sensors at $2,000–4,000. This ~60% price compression is driving Hesai and RoboSense into AMR and automotive design wins globally. US and Israeli LiDAR companies are responding with solid-state designs (higher reliability, lower cost at scale once tooled) and automotive-grade qualification as a differentiator. However, if Hesai achieves solid-state production before US players, it could extend its cost advantage into the next LiDAR architecture.

**FLIR as a non-tariff barrier:** Teledyne FLIR thermal camera modules (Boson, Lepton) are subject to US export controls under the EAR. This creates a practical barrier preventing Chinese drone and robot manufacturers from integrating them directly — a small but real competitive advantage for US-based drone companies (Skydio, Parrot ANAFI USA) in thermal-equipped platforms.

**Force/torque sensor niche:** ATI Industrial Automation (Apex Tool Group subsidiary), Robotiq (Quebec), and OnRobot (Denmark) supply the force/torque sensors used at robot wrists for compliant manipulation, assembly, and human-robot collaboration. This is a small-volume, high-value segment with limited competition and strong IP protection — a relatively defensible niche in an otherwise commoditizing sensor landscape.

### Supply Chain — Last Reviewed: 2026-03-24
