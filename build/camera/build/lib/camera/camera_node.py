import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraNode(Node):

    def __init__(self):
        super().__init__('depth_camera_node')

        # One-off parameters
        self.declare_parameter('period', 0.5)
        timer_period: float = self.get_parameter('period').get_parameter_value().double_value

        self.depth_camera_publisher = self.create_publisher(
            msg_type=Image,
            topic="/camera/image_raw",
            qos_profile=1)

        self.depth_camera_publisher = self.create_publisher(
            msg_type=Image,
            topic="/camera/detected_objects",
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

        node = CameraNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()