#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_msgs.msg import Odometry

import random
import json
from datetime import datetime


class TrackerNode(Node):
    def __init__(self):
        super().__init__('tracker_node')

        # Publishers
        self.location_pub = self.create_publisher(String, '/agri/location', 10)
        self.temperature_pub = self.create_publisher(String, '/agri/temperature', 10)
        self.humidity_pub = self.create_publisher(String, '/agri/humidity', 10)
        self.door_pub = self.create_publisher(String, '/agri/door', 10)
        self.battery_pub = self.create_publisher(String, '/agri/battery', 10)

        # Actual Gazebo vehicle position
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.position_received = False

        self.odom_sub = self.create_subscription(
            Odometry,
            '/model/agri_transport_vehicle/odometry',
            self.odom_callback,
            10
        )

        self.timer = self.create_timer(2.0, self.publish_readings)

        self.battery = 100.0
        self.door_open = False

        self.get_logger().info('Agri-Logistix Tracker Node started')

    def odom_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.z = msg.pose.pose.position.z
        self.position_received = True

    def publish_readings(self):

        # Publish actual simulated vehicle position
        if self.position_received:
            loc = String()
            loc.data = json.dumps({
                'x': round(self.x, 3),
                'y': round(self.y, 3),
                'z': round(self.z, 3),
                'coordinate_type': 'simulated_odometry_metres',
                'timestamp': datetime.now().isoformat()
            })
            self.location_pub.publish(loc)

        # Simulated temperature sensor
        temp = String()
        temp.data = str(round(random.uniform(5.0, 12.0), 2))
        self.temperature_pub.publish(temp)

        # Simulated humidity sensor
        hum = String()
        hum.data = str(round(random.uniform(60.0, 90.0), 2))
        self.humidity_pub.publish(hum)

        # Simulated door sensor
        if random.random() < 0.05:
            self.door_open = not self.door_open

        door = String()
        door.data = 'OPEN' if self.door_open else 'CLOSED'
        self.door_pub.publish(door)

        # Simulated battery
        self.battery -= 0.1

        if self.battery < 0:
            self.battery = 100.0

        batt = String()
        batt.data = str(round(self.battery, 1))
        self.battery_pub.publish(batt)

        if self.position_received:
            self.get_logger().info(
                f'POSITION {self.x:.2f}, {self.y:.2f} m'
                f' | TEMP {temp.data}C'
                f' | HUM {hum.data}%'
                f' | DOOR {door.data}'
                f' | BATT {batt.data}%'
            )
        else:
            self.get_logger().warning('Waiting for Gazebo odometry...')


def main(args=None):
    rclpy.init(args=args)
    node = TrackerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
