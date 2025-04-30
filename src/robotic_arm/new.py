import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import numpy as np
import time
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

class PickAndPlaceNode(Node):
    def __init__(self):
        super().__init__('pick_and_place_node')

        # Initialize robot          
        self.robot = InterbotixManipulatorXS(
            robot_model='px100',
            group_name='arm',
            gripper_name='gripper'
        )

        # Subscriber
        self.subscription = self.create_subscription(
            Point,
            '/object_position',
            self.object_position_callback,
            10)

        self.get_logger().info('Pick and Place Node Started.')

        # Go home
        self.robot.arm.go_to_home_pose()
        self.robot.gripper.release()

    def get_camera_to_base_transform(self):
        translation = np.array([0.1, 0.0, 0.2])
        rotation = np.eye(3)
        T_cam_to_base = np.eye(4)
        T_cam_to_base[0:3, 0:3] = rotation
        T_cam_to_base[0:3, 3] = translation
        return T_cam_to_base

    def transform_camera_to_base(self, position_in_camera):
        T_cam_to_base = self.get_camera_to_base_transform()
        pos_in_cam_homogeneous = np.append(position_in_camera, 1)
        pos_in_base_homogeneous = np.dot(T_cam_to_base, pos_in_cam_homogeneous)
        return pos_in_base_homogeneous[0:3]

    def move_to_pose(self, target_position):
        R_home = np.array([
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0]
        ])

        T_sd = np.eye(4)
        T_sd[0:3, 0:3] = R_home
        T_sd[0:3, 3] = target_position

        self.robot.arm.set_ee_pose_matrix(T_sd)

    def object_position_callback(self, msg):
        position_in_camera = np.array([msg.x, msg.y, msg.z])
        position_in_base = self.transform_camera_to_base(position_in_camera)
        self.get_logger().info(f"Object position (base frame): {position_in_base}")

        try:
            self.pick_object(position_in_base)
        except Exception as e:
            self.get_logger().error(f"Error: {e}")

    def pick_object(self, position_in_base):
        approach_position = position_in_base.copy()
        approach_position[2] += 0.05  # 5cm above

        self.move_to_pose(approach_position)
        time.sleep(0.5)

        self.move_to_pose(position_in_base)
        time.sleep(0.5)

        self.robot.gripper.grasp()
        time.sleep(0.5)

        lift_position = position_in_base.copy()
        lift_position[2] += 0.1  # Lift 10cm
        self.move_to_pose(lift_position)
        time.sleep(0.5)

        self.robot.arm.go_to_home_pose()
        self.robot.gripper.open()
        time.sleep(0.5)
        self.robot.arm.go_to_sleep_pose()

def main(args=None):
    rclpy.init(args=args)
    node = PickAndPlaceNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()