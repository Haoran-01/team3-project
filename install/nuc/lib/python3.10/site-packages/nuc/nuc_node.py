import rclpy
from rclpy.node import Node
from package_with_interfaces.msg import AmazingQuote
from sensor_msgs.msg import Imu, PointCloud2, Image
from std_msgs.msg import Bool
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, PoseStamped, PoseArray, Twist



class NUCNode(Node):

    def __init__(self):
        super().__init__('nuc_node')

        # One-off parameters
        self.declare_parameter('period', 0.5)
        timer_period: float = self.get_parameter('period').get_parameter_value().double_value

        self.task_goal_publisher = self.create_publisher(
            msg_type=PoseStamped,
            topic="/task/goal",
            qos_profile=1)

        self.arm_command_publisher = self.create_publisher(
            msg_type=PoseStamped,
            topic="/arm/command",
            qos_profile=1)

        self.cmd_vel_publisher = self.create_publisher(
            msg_type=Twist,
            topic="/navigation/cmd_vel",
            qos_profile=1)

        self.lidar_data_subscriber = self.create_subscription(
            msg_type=PointCloud2,
            topic='/lidar/scan',
            callback=self.lidar_data_callback,
            qos_profile=1)

        self.camera_data_subscriber = self.create_subscription(
            msg_type=Image,
            topic='/camera/image_raw',
            callback=self.camera_data_callback,
            qos_profile=1)

        self.arm_status_subscriber = self.create_subscription(
            msg_type=Bool,
            topic='/arm/status',
            callback=self.arm_status_callback,
            qos_profile=1)

        self.navigation_feedback_subscriber = self.create_subscription(
            msg_type=Odometry,
            topic='/navigation/feedback',
            callback=self.navigation_feedback_callback,
            qos_profile=1)


        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        pass

    def lidar_data_callback(self, msg: AmazingQuote):
        pass

    def camera_data_callback(self, msg: AmazingQuote):
        pass

    def arm_status_callback(self, msg: AmazingQuote):
        pass

    def navigation_feedback_callback(self, msg: AmazingQuote):
        pass


def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        node = NUCNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()