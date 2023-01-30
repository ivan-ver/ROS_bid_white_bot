#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Accel
from bid_wb_interfaces.msg import CurrentState


class Router(Node):
    def __init__(self) -> None:
        super().__init__("router")
        self.interface_subscriber = self.create_subscription(Accel, 'move_to_coordinates', self.listener_callback, 10)
        self.interface_publisher = self.create_publisher(Accel, 'publish_state', 10)
        self.current_state_publisher = self.create_publisher(CurrentState, 'current_state', 10)
        self.create_timer(0.5, self.publish_current_state)

    def listener_callback(self, msg: Accel) -> None:
        self.get_logger().info('I heard: "%s"' % msg)
        self.interface_publisher.publish(msg)

    def publish_current_state(self):
        current_state = CurrentState()
        current_state.coordinates.x = 800.0
        current_state.coordinates.y = 500.0
        current_state.coordinates.z = 500.0
        current_state.alpha_angle = 45.0
        current_state.betta_angle = 45.0
        current_state.current_engine_tics = [654, 258, 317, 943, 234, 745]
        self.current_state_publisher.publish(current_state)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = Router()
    rclpy.spin(node)
    rclpy.shutdown()
