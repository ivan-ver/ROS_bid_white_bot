#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from bid_wb_interfaces.action import InverseKinematic


class InverseKinematicAction(Node):
    def __init__(self) -> None:
        super().__init__('inverse_kinematic_action')
        self.get_logger().info(f"inverse_kinematic_service is running")
        # self.ikService = self.create_service(InverseKinematic, 'get_angles_from_coordinates', self.calculate_ik)
        self.ikService = self._action_server = ActionServer(self, InverseKinematic, 'get_angles_from_coordinates',
                                                            self.calculate_ik)

    def calculate_ik(self, goal_handle):
        feedback_msg = InverseKinematic.Feedback()

        for i in range(5):
            feedback_msg.angles.append(1)
            feedback_msg.angles.append(2)
            feedback_msg.angles.append(3)
            goal_handle.publish_feedback(feedback_msg)
        res = InverseKinematic.Result()
        res.result = feedback_msg.angles
        return res


def main(args=None) -> None:
    rclpy.init(args=args)
    node = InverseKinematicAction()
    rclpy.spin(node)
    rclpy.shutdown()
