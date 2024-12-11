import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu


class IMUNode(Node):

    def __init__(self):
        super().__init__('imu_node')

        # One-off parameters
        self.declare_parameter('period', 0.5)
        timer_period: float = self.get_parameter('period').get_parameter_value().double_value

        self.cmd_vel_publisher = self.create_publisher(
            msg_type=Imu,
            topic="/imu/data",
            qos_profile=1)

        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        pass

def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        node = IMUNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()