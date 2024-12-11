import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Image
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry, Path
from std_msgs.msg import String


class ControllerServerNode(Node):

    def __init__(self):
        super().__init__('controller_server_node')

        # One-off parameters
        self.declare_parameter('period', 0.5)
        timer_period: float = self.get_parameter('period').get_parameter_value().double_value

        self.motor_cmd_vel_publisher = self.create_publisher(
            msg_type=Twist,
            topic="/motor/cmd_vel",
            qos_profile=1)

        self.controller_status_publisher = self.create_publisher(
            msg_type=String,
            topic="/controller/status",
            qos_profile=1)


        self.cmd_vel_subscriber = self.create_subscription(
            msg_type=Twist,
            topic='/cmd_vel',
            callback=self.cmd_vel_callback,
            qos_profile=1)


        self.odom_subscriber = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.odom_callback,
            qos_profile=1)


        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        pass

    def cmd_vel_callback(self, msg: PointCloud2):
        pass

    def task_goal_callback(self, msg: PoseStamped):
        pass

    def odom_callback(self, msg: PoseStamped):
        pass


def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        node = ControllerServerNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()