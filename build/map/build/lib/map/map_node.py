'''/map（nav_msgs/OccupancyGrid）：环境的占据网格地图。
订阅：
/lidar/depth（sensor_msgs/PointCloud2）：使用深度数据更新地图。
/camera/detected_objects（custom_msgs/ObjectArray）：结合目标信息更新地图。
"'''


import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Image
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry, Path, OccupancyGrid


class MapNode(Node):

    def __init__(self):
        super().__init__('navigation_node')

        # One-off parameters
        self.declare_parameter('period', 0.5)
        timer_period: float = self.get_parameter('period').get_parameter_value().double_value

        self.map_publisher = self.create_publisher(
            msg_type=OccupancyGrid,
            topic="/map",
            qos_profile=1)

        self.scan_data_subscriber = self.create_subscription(
            msg_type=PointCloud2,
            topic='/scan',
            callback=self.scan_data_callback,
            qos_profile=1)

        self.camera_detected_subscriber = self.create_subscription(
            msg_type=Image,
            topic='/camera/detected_objects',
            callback=self.camera_detected_callback,
            qos_profile=1)


        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        pass

    def scan_data_callback(self, msg: PointCloud2):
        pass

    def camera_detected_callback(self, msg: PoseStamped):
        pass


def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        node = MapNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()