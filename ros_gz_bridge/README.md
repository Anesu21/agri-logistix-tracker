# Agri-Logistix ROS-Gazebo Bridge

This bridge transfers the simulated vehicle's odometry from Gazebo
to ROS 2.

## Requirements
- ROS 2 Lyrical
- Gazebo Sim
- ros_gz_bridge
- nav_msgs

## Start

Start the Agri-Logistix Gazebo world first, then open another terminal:

```bash
source /opt/ros/lyrical/setup.bash
./ros_gz_bridge/start_bridge.sh
```

The bridge maps:

| Gazebo topic | ROS 2 topic |
|---|---|
| /model/agri_transport_vehicle/odometry | /model/agri_transport_vehicle/odometry |

Message conversion:

- Gazebo: gz.msgs.Odometry
- ROS 2: nav_msgs/msg/Odometry

## Verify

```bash
ros2 topic list
ros2 topic echo /model/agri_transport_vehicle/odometry
```

The bridge must be running while Gazebo publishes the vehicle odometry.
