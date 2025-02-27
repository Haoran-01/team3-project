import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from ultralytics import YOLO
from geometry_msgs.msg import PoseStamped  # 用于发布目标位置
from std_msgs.msg import String

class YOLOv8RealSenseNode(Node):
    def __init__(self):
        super().__init__('yolo_realsense_node')

        # Subscribe to RealSense Color Imaging Topic
        self.sub_color = self.create_subscription(
            Image, '/camera/camera/color/image_raw', self.image_callback_color, 10)

        # Subscribe to RealSense Depth Imaging Topic
        self.sub_depth = self.create_subscription(
            Image, '/camera/camera/depth/image_rect_raw', self.image_callback_depth, 10)

        # Post target location & target category
        self.pub_target_position = self.create_publisher(PoseStamped, "/robot/target_position", 10)
        self.pub_target_class = self.create_publisher(String, "/robot/target_class", 10)


        # initial OpenCV
        self.bridge = CvBridge()

        # upload YOLOv8 model
        self.model = YOLO("best_copy.pt")

        # Stores the most recent frame of RGB and depth data
        self.color_image = None
        self.depth_image = None

        self.get_logger().info("✅ YOLOv8 RealSense Object Detection + Depth Measurement Node Launch")

    def image_callback_color(self, msg):
        """ Processing color images and running YOLO target detection """
        self.color_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        frame = self.color_image.copy()

        results = self.model(frame)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get detection box
                class_id = int(box.cls[0])  # Get category index
                conf = float(box.conf[0])  # Get Confidence

                # Calculate target center point
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                # Get object depth value
                depth = self.get_depth_value(center_x, center_y)

                # Plotting detection frames and depth information
                label = f"{self.model.names[class_id]} {conf:.2f} - {depth:.2f}m"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 2)

        # show the detection answer
        cv2.imshow("YOLOv8 RealSense Detection", frame)
        cv2.waitKey(1)

    def image_callback_depth(self, msg):
        """ Processing depth images """
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, "16UC1")  # 16-bit

    def get_depth_value(self, x, y):
        if self.depth_image is not None:
            # Get depth image size
            depth_h, depth_w = self.depth_image.shape

            # Get RGB image size
            rgb_h, rgb_w, _ = self.color_image.shape

            # Calculating scaling
            scale_x = depth_w / rgb_w  # 848 / 1280
            scale_y = depth_h / rgb_h  # 480 / 720

            # Calculate the coordinates in the depth map
            depth_x = int(x * scale_x)
            depth_y = int(y * scale_y)

            # Ensure that the coordinates are not out of range
            depth_x = np.clip(depth_x, 0, depth_w - 1)
            depth_y = np.clip(depth_y, 0, depth_h - 1)

            depth_value = self.depth_image[depth_y, depth_x]

            # Processing of invalid depths (0 indicates invalid data)
            if depth_value == 0:
                print(f"invalid depths value ({depth_x}, {depth_y}), try the surrounding pixels")

                # Finding the nearest effective depth in a 3x3 neighborhood
                kernel_size = 3
                half_k = kernel_size // 2
                valid_depths = []

                for i in range(-half_k, half_k + 1):
                    for j in range(-half_k, half_k + 1):
                        new_x = np.clip(depth_x + i, 0, depth_w - 1)
                        new_y = np.clip(depth_y + j, 0, depth_h - 1)
                        neighbor_depth = self.depth_image[new_y, new_x]
                        if neighbor_depth > 0:
                            valid_depths.append(neighbor_depth)

                if valid_depths:
                    depth_value = np.median(valid_depths)  # Take the median depth of the neighborhood
                else:
                    print("Still no valid depth, return -1")
                    return -1


            depth_meters = depth_value / 1000.0  # Convert to meters
            return depth_meters
        else:
            return -1


    def publish_target_position(self, X, Y, Z, class_id):
            """ 发布目标位置 & 目标类别 """
            if Z < 0:
                return  # 目标深度无效，跳过

            # 创建目标位置消息
            target_pose = PoseStamped()
            target_pose.header.stamp = self.get_clock().now().to_msg()
            target_pose.pose.position.x = X
            target_pose.pose.position.y = Y
            target_pose.pose.position.z = Z
            self.pub_target_position.publish(target_pose)

            # 目标类别
            target_class = String()
            target_class.data = self.model.names[class_id]
            self.pub_target_class.publish(target_class)

            self.get_logger().info(f"📍 目标: {target_class.data}, 位置: ({X:.2f}, {Y:.2f}, {Z:.2f})")




def main(args=None):
    rclpy.init(args=args)
    node = YOLOv8RealSenseNode()
    rclpy.spin(node)

    node.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
