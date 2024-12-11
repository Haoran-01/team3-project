import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry, Path


class NavigationNode(Node):

    def __init__(self):
        super().__init__('navigation_node')

        # One-off parameters
        self.declare_parameter('period', 0.5)
        timer_period: float = self.get_parameter('period').get_parameter_value().double_value

        self.nav_path_publisher = self.create_publisher(
            msg_type=Path,
            topic="/navigation/path",
            qos_profile=1)

        self.nav_feedback_publisher = self.create_publisher(
            msg_type=Odometry,
            topic="/navigation/feedback",
            qos_profile=1)

        self.nav_cmd_vel_publisher = self.create_publisher(
            msg_type=Twist,
            topic="/navigation/cmd_vel",
            qos_profile=1)

        self.scan_data_subscriber = self.create_subscription(
            msg_type=PointCloud2,
            topic='/scan',
            callback=self.scan_data_callback,
            qos_profile=1)

        self.task_goal_subscriber = self.create_subscription(
            msg_type=PoseStamped,
            topic='/task/goal',
            callback=self.task_goal_callback,
            qos_profile=1)


        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        pass

    def scan_data_callback(self, msg: PointCloud2):
        pass

    def task_goal_callback(self, msg: PoseStamped):
        pass


def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        node = NavigationNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()