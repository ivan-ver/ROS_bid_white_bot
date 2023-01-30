#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node


class InverseKinematicCalculator(Node):
    def __init__(self) -> None:
        super().__init__('inverse_kinematic_calculator_server')
        self._action_server = ActionServer(self, Fibonacci, 'fibonacci', self.execute_callback)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = InverseKinematicCalculator()
    rclpy.spin(node)
    rclpy.shutdown()
