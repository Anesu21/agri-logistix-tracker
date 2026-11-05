#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class AlertNode(Node):
    def __init__(self):
        super().__init__('alert_node')
        self.create_subscription(String, '/agri/temperature', self.check_temperature, 10)
        self.create_subscription(String, '/agri/humidity', self.check_humidity, 10)
        self.create_subscription(String, '/agri/door', self.check_door, 10)
        self.create_subscription(String, '/agri/battery', self.check_battery, 10)
        self.alert_pub = self.create_publisher(String, '/agri/alerts', 10)
        self.get_logger().info('Agri-Logistix Alert Node started')

    def send_alert(self, alert_type, severity, message):
        alert = String()
        alert.data = '[' + severity + '] ' + alert_type + ': ' + message
        self.alert_pub.publish(alert)
        self.get_logger().warn(alert.data)

    def check_temperature(self, msg):
        try:
            temp = float(msg.data)
            if temp > 12.0:
                self.send_alert('TEMPERATURE', 'HIGH', str(temp) + 'C exceeds 12C')
            elif temp < 5.0:
                self.send_alert('TEMPERATURE', 'HIGH', str(temp) + 'C below 5C')
        except ValueError:
            pass

    def check_humidity(self, msg):
        try:
            hum = float(msg.data)
            if hum > 90.0:
                self.send_alert('HUMIDITY', 'MEDIUM', str(hum) + '% exceeds 90%')
            elif hum < 60.0:
                self.send_alert('HUMIDITY', 'MEDIUM', str(hum) + '% below 60%')
        except ValueError:
            pass

    def check_door(self, msg):
        if msg.data == 'OPEN':
            self.send_alert('DOOR', 'HIGH', 'Door opened during transit')

    def check_battery(self, msg):
        try:
            batt = float(msg.data)
            if batt < 20.0:
                self.send_alert('BATTERY', 'MEDIUM', 'Battery low: ' + str(batt) + '%')
        except ValueError:
            pass


def main(args=None):
    rclpy.init(args=args)
    node = AlertNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
