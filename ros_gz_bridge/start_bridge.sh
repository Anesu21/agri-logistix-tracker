#!/usr/bin/env bash
set -e

source /opt/ros/lyrical/setup.bash

echo "Starting Agri-Logistix Gazebo-to-ROS odometry bridge..."

exec ros2 run ros_gz_bridge parameter_bridge \
  '/model/agri_transport_vehicle/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry'
