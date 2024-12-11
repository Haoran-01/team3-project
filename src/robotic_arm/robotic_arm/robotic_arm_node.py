import rclpy
from rclpy.node import Node
from package_with_interfaces.msg import AmazingQuote
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool


class RoboticArmNode(Node):

    def __init__(self):
        super().__init__('robotic_arm_node')

        # One-off parameters
        self.declare_parameter('period', 0.5)
        timer_period: float = self.get_parameter('period').get_parameter_value().double_value

        self.arm_status_publisher = self.create_publisher(
            msg_type=Bool,
            topic="/arm/status",
            qos_profile=1)

        self.task_goal_subscriber = self.create_subscription(
            msg_type=PoseStamped,
            topic='/task/goal',
            callback=self.task_goal_callback,
            qos_profile=1)

        self.arm_command_subscriber = self.create_subscription(
            msg_type=PoseStamped,
            topic='/arm/command',
            callback=self.arm_command_callback,
            qos_profile=1)


        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        pass

    def task_goal_callback(self, msg: AmazingQuote):
        pass

    def arm_command_callback(self, msg: AmazingQuote):
        pass


def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        node = RoboticArmNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()