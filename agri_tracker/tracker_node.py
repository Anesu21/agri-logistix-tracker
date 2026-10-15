#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import json
from datetime import datetime


class TrackerNode(Node):
    def __init__(self):
        super().__init__('tracker_node')
        self.location_pub = self.create_publisher(String, '/agri/location', 10)
        self.temperature_pub = self.create_publisher(String, '/agri/temperature', 10)
        self.humidity_pub = self.create_publisher(String, '/agri/humidity', 10)
        self.door_pub = self.create_publisher(String, '/agri/door', 10)
        self.battery_pub = self.create_publisher(String, '/agri/battery', 10)
        self.timer = self.create_timer(2.0, self.publish_readings)
        self.latitude = -17.8252
        self.longitude = 31.0335
        self.battery = 100.0
        self.door_open = False
        self.get_logger().info('Agri-Logistix Tracker Node started')

    def publish_readings(self):
        self.latitude += random.uniform(-0.0001, 0.0001)
        self.longitude += random.uniform(-0.0001, 0.0001)
        loc = String()
        loc.data = json.dumps({'latitude': round(self.latitude, 6), 'longitude': round(self.longitude, 6), 'timestamp': datetime.now().isoformat()})
        self.location_pub.publish(loc)
        temp = String()
        temp.data = str(round(random.uniform(5.0, 12.0), 2))
        self.temperature_pub.publish(temp)
        hum = String()
        hum.data = str(round(random.uniform(60.0, 90.0), 2))
        self.humidity_pub.publish(hum)
        if random.random() < 0.05:
            self.door_open = not self.door_open
        door = String()
        door.data = 'OPEN' if self.door_open else 'CLOSED'
        self.door_pub.publish(door)
        self.battery -= 0.1
        if self.battery < 0:
            self.battery = 100.0
        batt = String()
        batt.data = str(round(self.battery, 1))
        self.battery_pub.publish(batt)
        self.get_logger().info('LOC ' + str(round(self.latitude,4)) + ',' + str(round(self.longitude,4)) + ' | TEMP ' + temp.data + 'C | HUM ' + hum.data + '% | DOOR ' + door.data + ' | BATT ' + batt.data + '%')


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
