import rclpy
from rclpy.node import Node
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from package_with_interfaces.msg import TargetBlock
import numpy as np
import time

# Set workspace constraints
Z_MIN = 0.02  # Minimum Z value (above base level)
Z_MAX = 0.25  # Maximum reach of PX100

class PickAndPlaceNode(Node):
    def __init__(self):
        super().__init__('px100_pick_and_place')
        
        # Initialize the robot arm
        self.bot = InterbotixManipulatorXS("px100", "arm", "gripper")
        
        self.get_logger().info("Waiting for object position...")
        
        # Create a subscriber for target block positions
        self.subscription = self.create_subscription(
            TargetBlock,
            '/robot/target_position',
            self.target_position_callback,
            10)
        
    def target_position_callback(self, msg):
        object_x = msg.position.pose.position.x
        object_y = msg.position.pose.position.y
        object_z = max(msg.position.pose.position.z, Z_MIN)  # Ensure Z is within limits
        object_type = msg.type  # "block" or "bin"
        object_color = msg.color

        self.get_logger().info(f"Received target: {object_color} {object_type} at x={object_x}, y={object_y}, z={object_z}")

        if object_type != "block":
            self.get_logger().warn("Skipping non-block objects.")
            return

        if not self.is_within_workspace(object_x, object_y, object_z):
            self.get_logger().warn("Target position is outside the workspace.")
            return
        
        # Move to pick position
        success = self.bot.arm.set_ee_pose_components(x=object_x, y=object_y, z=object_z)
        if not success:
            self.get_logger().warn("IK solution not found for pick position.")
            return
        time.sleep(1)
        
        # Close gripper to pick object
        self.bot.gripper.grasp()
        time.sleep(1)

        # Define place position based on color (Modify as needed)
        place_positions = {
            "blue": [0.2, 0.2, 0.1],
            "yellow": [0.1, 0.2, 0.1],
            "green": [0.2, 0.1, 0.1],
        }
        place_position = place_positions.get(object_color, [0.2, 0.2, 0.1])  
        
        # Move to place position
        success = self.bot.arm.set_ee_pose_components(x=place_position[0], y=place_position[1], z=place_position[2])
        if not success:
            self.get_logger().warn("IK solution not found for place position.")
            return
        time.sleep(1)

        # Release object
        self.bot.gripper.release()
        time.sleep(1)

        # Return to home position
        self.bot.arm.go_to_home_pose()
    
    def is_within_workspace(self, x, y, z):
        r = np.sqrt(x**2 + y**2)
        z_min, z_max = Z_MIN, Z_MAX
        r_min, r_max = 0.05, 0.3  # Modify based on reach
        return (r_min <= r <= r_max) and (z_min <= z <= z_max)


def main(args=None):
    """
    The main function.

    :param args: Not used directly by the user, but used by ROS2 to configure certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        # Initialize the PickAndPlaceNode
        node = PickAndPlaceNode()

        # Spin the node to keep it running
        rclpy.spin(node)
    
    except KeyboardInterrupt:
        pass
    except Exception as e:
        # Print any exceptions that occur during node execution
        print(f"An error occurred: {e}")
    
    finally:
        # Clean up and shutdown ROS2 when done
        if rclpy.ok():
            node.destroy_node()  # Destroy the node to clean up resources
            rclpy.shutdown()     # Shutdown rclpy

if __name__ == '__main__':
    main()
