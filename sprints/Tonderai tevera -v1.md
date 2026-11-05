# Sprint 1 - Tonderai Tevera

**Student:** Tonderai Tevera
**Reg No:** N02530022R 
**Project:** Agri-Logistix Tracker - IoT Cold Chain Monitoring
**File:** Tonderai-tevera-v1.md
**Date:** 22 Oct 2026

## Contribution
- Cloned repo Anesu21/agri-logistix-tracker
- Created my Sprint 1 file in sprints/ folder
- Committed to main branch before 14:00 deadline

## Physical Mapping Summary (from whiteboard)
AGRI-LOGISTIX is a $40 IoT tracker for perishable food transport.

**Hardware:**
- ESP32 (the Brain) - center of breadboard, reads all sensors
- Power: Battery (3.7V) -> Power Module (Buck Converter 5V) -> +5V rail (red) and GND rail (blue)
- GPS: Tracks truck location (TX->RX, RX->TX, 5V, GND)
- DHT22: Air Temp & Humidity inside container
- DS18B20: Waterproof probe - actual food temperature
- Door Switch: Magnetic switch - detects door open/close
- GSM SIM800L: Sends data via Mobile Network -> Cloud Platform -> Dashboard Alerts

**Data Flow:** Sensors -> ESP32 -> GSM -> Mobile Network -> Cloud -> Dashboard (Farmer sees TEMP, HUMIDITY, DOOR status + GPS)

**Purpose:** Prevent spoilage - if temp > 4°C or door opened, alert sent with GPS location.

## Notes
All power and grounds connect to the breadboard rails. Off-the-shelf parts. Easy breadboard connections, no soldering needed. ROS2 + Gazebo used for simulation, this board is real physical deployment on refrigerated truck.