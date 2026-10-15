# Agri-Logistix Tracker Simulation

## Project
IoT tracker simulation for perishable food transport - monitors GPS, temperature, humidity, door events, and battery in real time.

## Team
- Anesu Mugweni
- NUST Email: n02530952v@students.nust.ac.zw
- Ezra Kufazvineyi
- Nust Email: n02531364l@students.nust.ac.zw
- Tonderai Tevera
- Nust email :n02530022R@students.nust.ac.zw
- Rasheed Phiri
- Nust email :N02530037H@students.nust.ac.zw

## System Specifications
- OS: Ubuntu 22.04 (The Construct Rosject)
- ROS2 Version: Humble Hawksbill
- Language: Python 3.10
- Simulation: Gazebo (available)

## Installation Instructions

The project runs inside The Construct cloud ROS2 environment with ROS2 Humble pre-installed.

To replicate on Ubuntu 22.04 with ROS2 Humble:

sudo apt update
sudo apt install -y ros-humble-desktop
source /opt/ros/humble/setup.bash

## Execution Instructions

### 1. Build the workspace
cd ~/ros2_ws
colcon build
source install/setup.bash

### 2. Run the tracker node - Terminal 1
source ~/ros2_ws/install/setup.bash
ros2 run agri_tracker tracker_node

### 3. Run the alert node - Terminal 2
source ~/ros2_ws/install/setup.bash
ros2 run agri_tracker alert_node

### 4. Monitor alerts - Terminal 3
source ~/ros2_ws/install/setup.bash
ros2 topic echo /agri/alerts

## ROS2 Topics Published

- /agri/location - GPS coordinates
- /agri/temperature - Cargo temperature - safe 5-12C
- /agri/humidity - Cargo humidity - safe 60-90 percent
- /agri/door - Door state OPEN or CLOSED
- /agri/battery - Tracker battery level
- /agri/alerts - Generated alerts

## Alert Conditions

- Temperature outside 5-12C range - HIGH severity
- Humidity outside 60-90 percent range - MEDIUM severity
- Door opened during transit - HIGH severity
- Battery below 20 percent - MEDIUM severity

## Project Structure

agri_tracker/
  agri_tracker/
    __init__.py
    tracker_node.py
    alert_node.py
  resource/
  test/
  package.xml
  setup.py
  README.md
