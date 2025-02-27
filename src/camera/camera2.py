import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImageDepthSubscriber(Node):
    def __init__(self, name):
        super().__init__(name)
        # 订阅颜色图像
        self.sub_color = self.create_subscription(
            Image, '/camera/camera/color/image_raw', self.listener_callback_color, 10
        )
        # 订阅深度图像
        self.sub_depth = self.create_subscription(
            Image, '/camera/camera/depth/image_rect_raw', self.listener_callback_depth, 10
        )

        self.cv_bridge = CvBridge()
        self.color_image = None  # 缓存最近的一帧颜色图像
        self.depth_image = None  # 缓存最近的一帧深度图像
        self.color_count = 0
        self.save_path = "/home/mscrobotics2425laptop14/Desktop/project/team3/team3-project/src/camera/captured_images/color2/"
        self.save_path2 = "/home/mscrobotics2425laptop14/Desktop/project/team3/team3-project/src/camera/captured_images/depth2/"

    def listener_callback_color(self, data):
        """ 订阅颜色图像并缓存最新帧 """
        self.color_image = self.cv_bridge.imgmsg_to_cv2(data, 'bgr8')
        self.display_images()  # 实时显示图像，并监听按键

    def listener_callback_depth(self, data):
        """ 订阅深度图像并缓存最新帧 """
        self.depth_image = self.cv_bridge.imgmsg_to_cv2(data, '16UC1')  # 16位深度图
        self.display_images()  # 实时显示图像，并监听按键

    def display_images(self):
        """ 实时显示摄像头画面，并监听按键输入 """
        if self.color_image is None or self.depth_image is None:
            return  # 需要同时收到 RGB 和深度图像后才显示

        # 把深度图像转换成可视化的灰度图（缩放到 8bit）
        depth_visual = cv2.normalize(self.depth_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        # 显示两个窗口：RGB 和 深度
        cv2.imshow("Color Image (Press 's' to Save)", self.color_image)
        cv2.imshow("Depth Image (Press 's' to Save)", depth_visual)

        # 监听键盘输入
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # 按 `s` 键保存图像
            self.save_images()
        elif key == ord('q'):  # 按 `q` 退出
            self.get_logger().info("退出程序")
            cv2.destroyAllWindows()
            rclpy.shutdown()

    def save_images(self):
        """ 同时保存颜色图像和深度图像 """
        if self.color_image is None or self.depth_image is None:
            self.get_logger().warn("图像未准备好，无法保存")
            return

        # 生成文件名
        color_file = f"{self.save_path}color_{self.color_count}.jpg"
        depth_file = f"{self.save_path2}depth_{self.color_count}.png"

        # 保存 RGB 图像
        cv2.imwrite(color_file, self.color_image)
        # 保存深度图像
        cv2.imwrite(depth_file, self.depth_image)

        self.get_logger().info(f"✅ 已保存颜色图像: {color_file}")
        self.get_logger().info(f"✅ 已保存深度图像: {depth_file}")

        self.color_count += 1  # 计数增加


def main(args=None):
    rclpy.init(args=args)
    node = ImageDepthSubscriber("image_depth_sub")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("节点被终止")
    finally:
        node.destroy_node()
        cv2.destroyAllWindows()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
