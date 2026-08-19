---
title: "Open Source Drone Detection Projects"
date: 2026-06-05
lastmod: 2026-08-15
draft: false
description: "Open-source tools and libraries for drone detection, Remote ID decoding, radar, and multi-camera vision tracking — usable today for building custom detection systems."
research_area: "drone-detection/open-source"
last_reviewed: 2026-08-15
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.7
  disable: false
---

# Open Source Drone Detection Projects

Active open-source projects for drone detection and Remote ID decoding. Filtered for projects that are functional and usable today.

## Projects

- [OpenDroneID]({{< relref "opendroneid.md" >}}) — ASTM F3411 encode/decode library; Android receiver; Linux transmitter
- [DJI DroneID Decoder]({{< relref "dji-droneid-decoder.md" >}}) — GNU Radio / SDR decoder for proprietary DJI DroneID (pre-Remote ID)
- [ArduPilot RemoteID]({{< relref "ardupilot-remoteid.md" >}}) — Open-source Remote ID transmitter for ArduPilot-based drones
- [Acoustic ML Pipeline]({{< relref "acoustic-ml-pipeline.md" >}}) — Raspberry Pi + MEMS mic array + CNN/Random Forest classifier; detects RF-dark drones acoustically
- [Mesh-Mapper]({{< relref "mesh-mapper.md" >}}) — Dual-core ESP32 WiFi/BT Remote ID detector; Flask web map; Meshtastic mesh alerting; FAA lookup
- [DragonSync]({{< relref "dragonsync.md" >}}) — Fuses Remote ID + DJI DroneID detections into CoT for TAK/ATAK, MQTT/Home Assistant, and Lattice; software core of the WarDragon kit
- [iNTERCEPT]({{< relref "intercept.md" >}}) — Broad web-based SIGINT platform (ADS-B, AIS, pagers, weather sat, and more) with a multi-vector drone-detection module
- [Phantom-Proof]({{< relref "phantom-proof.md" >}}) — Cross-verifies Remote ID claims against passive radar tracks to flag spoofed (PHANTOM) or contradictory (DECEPTION) broadcasts
- [droneRemoteIDSpoofer]({{< relref "drone-remoteid-spoofer.md" >}}) — WiFi/BLE Remote ID spoofer for testing receiver systems; demonstrates the protocol's lack of authentication
- [AERIS-10 (PLFM_RADAR)]({{< relref "aeris-10-radar.md" >}}) — Open-source 10.5 GHz phased array PLFM radar; 3 km/20 km variants; electronic beam steering; FPGA Doppler/CFAR processing — detects RF-silent drones; accepted by Crowd Supply for a Q3 2026 crowdfunding launch
- [Stereo Drone Tracker]({{< relref "stereo-drone-tracker.md" >}}) — Real-time stereo-camera (2× IMX477) YOLOv11 detection + 3D triangulation + Kalman/Hungarian tracking with occlusion re-ID; Jetson Orin Nano; ~$550 build
- [UAV Detection and Tracking]({{< relref "uav-detection-and-tracking.md" >}}) — Single-camera Faster R-CNN detection + Kalman filter 2D trajectory tracking/visualization
- [eye_sky]({{< relref "eye-sky.md" >}}) — Python multi-camera, multi-object tracker with binocular 3D triangulation; Python port of SPOTIT3D; two associated peer-reviewed papers
- [Drone Tracking Datasets]({{< relref "drone-tracking-datasets.md" >}}) — RTK-ground-truthed multi-view drone benchmark dataset (5 sequences, 4–7 cameras); paired `mvus` unsynchronized-camera 3D reconstruction pipeline
- [Topology-Aware Multi-Camera Tracking]({{< relref "topology-aware-multi-camera-tracking.md" >}}) — Cross-camera vehicle re-ID/handover framework (adjacent technique, not drone-specific); YOLO + ByteTrack; non-commercial license

## Quick Reference: What Each Project Does

| Project | Language/Platform | Function | Status |
|---------|------------------|----------|--------|
| opendroneid-core-c | C | ASTM F3411 encode/decode library | Active |
| receiver-android | Android/Java | Decode BRI from Wi-Fi NAN + BT5 | Active |
| proto17/dji_droneid | GNU Radio / MATLAB | Decode proprietary DJI DroneID | Active (community) |
| ArduPilot/ArduRemoteID | C++ / ArduPilot | Transmit Remote ID from ArduPilot drones | Active |
| PiNcH | Python | Drone presence detection via network traffic analysis (ArduCopter) | Research |
| RPi acoustic ML pipeline | Python / scikit-learn / TFLite | MEMS mic array + MFCC + Random Forest/CNN for passive acoustic detection | DIY / Research |
| Mesh-Mapper | ESP32 (dual-core) / Python Flask | WiFi+BT Remote ID capture, web map, Meshtastic mesh relay, FAA lookup | Active |
| DragonSync | Python | Fuses Remote ID/DJI DroneID detections into CoT, MQTT/HA, Lattice | Active |
| iNTERCEPT | Python / Flask | Multi-domain SIGINT platform; drone module (Remote ID + sub-GHz + 2.4/5.8GHz) | Active |
| Phantom-Proof | Python | Passive-radar physical verification of Remote ID claims (anti-spoofing) | Early-stage |
| droneRemoteIDSpoofer | Python / scapy | WiFi + BLE Remote ID spoofer for testing detection/receiver systems | Active |
| AERIS-10 (PLFM_RADAR) | VHDL/Verilog (FPGA) + C (STM32) + Python | Open-source 10.5 GHz phased array PLFM radar; electronic beam steering; onboard Doppler/CFAR | Alpha; Crowd Supply campaign targeted Q3 2026 |
| Stereo Drone Tracker | Python / TensorRT (Jetson) | Stereo YOLOv11 detection + 3D triangulation + Kalman/Hungarian tracking, occlusion re-ID | Active; early-stage (0 stars) |
| UAV Detection and Tracking | Python / TensorFlow 2 | Faster R-CNN detection + Kalman filter 2D trajectory tracking | Active |
| eye_sky | Python / OpenCV | Multi-camera multi-object tracking + binocular 3D triangulation | Active; small |
| Drone Tracking Datasets (+ mvus) | Python | RTK-ground-truthed multi-view drone dataset + unsynchronized-camera 3D reconstruction pipeline | Active; well-adopted (213★ dataset / 89★ mvus) |
| Topology-Aware Multi-Camera Tracking | Python / Ultralytics YOLO + ByteTrack | Cross-camera vehicle tracking with topology-aware ID handover (adjacent technique) | Active; non-commercial license |
