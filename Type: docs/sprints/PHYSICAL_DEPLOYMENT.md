# Physical Deployment of DROID - Agri-Logistix

## Hardware
- DROID: 4WD chassis + GPS NEO-6M + ESP32 + LoRa
- Power: 12V battery + solar

## Deployment Diagram
Tractor (DROID) -> GPS -> ESP32 (ROS2 node) -> LoRa -> Gateway -> Cloud -> Dashboard

## Environment
- Field: NUST Farm
- Gazebo model: farm_world.sdf simulates deployment

## Install to run physical
ros2 launch agri_logistix_tracker deploy.launch.py
