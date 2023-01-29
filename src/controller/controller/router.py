#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, MultiArrayLayout
from bid_wb_interfaces.msg import TargetInfo
from geometry_msgs.msg import Accel


class Router(Node):
    def __init__(self) -> None:
        super().__init__("router")
        self.interface_subscriber = self.create_subscription(Accel, 'move_to_coordinates', self.listener_callback, 10)
        self.interface_publisher = self.create_publisher(Accel, 'publish_state', 10)

    def listener_callback(self, msg: Accel) -> None:
        self.get_logger().info('I heard: "%s"' % msg)
        self.interface_publisher.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = Router()
    rclpy.spin(node)
    rclpy.shutdown()
