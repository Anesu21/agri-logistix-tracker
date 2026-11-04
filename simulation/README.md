# Agri-Logistix Gazebo Simulation

## Overview

This directory contains the Gazebo farm environment and autonomous vehicle controller for the Agri-Logistix fleet management system.

The simulation represents a vehicle transporting perishable goods within a farm environment.

## Directory Structure

```text
simulation/
├── README.md
├── create_world.py
├── worlds/
│   └── agri_farm.sdf
└── scripts/
    └── autonomous_driver.py
```

## Requirements

- Ubuntu Linux
- Gazebo Sim
- Python 3
- Gazebo command-line tools (`gz`)

## Running the Simulation

### Step 1: Open the farm environment

Open a terminal in the repository directory:

```bash
cd ~/agri-logistix-tracker
```

Launch Gazebo:

```bash
gz sim -r simulation/worlds/agri_farm.sdf
```

Wait for the environment and vehicle to load.

### Step 2: Start the autonomous vehicle

Open a second terminal:

```bash
cd ~/agri-logistix-tracker
```

Run:

```bash
python3 simulation/scripts/autonomous_driver.py
```

### Step 3: Observe the autonomous route

The vehicle performs the following sequence:

1. Moves forward.
2. Turns left.
3. Moves forward again.
4. Turns right.
5. Stops and parks.

## Vehicle Control

The vehicle uses the Gazebo DiffDrive plugin.

Command topic:

`/model/agri_transport_vehicle/cmd_vel`

Odometry topic:

`/model/agri_transport_vehicle/odometry`

## Notes

- Launch Gazebo before starting the autonomous driver.
- Keep the Gazebo terminal running while the vehicle controller is active.
- The autonomous driver publishes repeated velocity commands during each movement stage.
- This simulation is designed for future integration with the ROS2 tracking and fleet management components.
