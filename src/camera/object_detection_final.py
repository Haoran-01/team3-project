import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
import cv2
import numpy as np
from ultralytics import YOLO
from geometry_msgs.msg import PoseStamped  # 发送目标 3D 坐标
from std_msgs.msg import String  # 发送目标类别
from package_with_interfaces.msg import TargetBlock

class YOLOv8RealSenseNode(Node):
    def __init__(self):
        super().__init__('yolo_realsense_node')

        # Subscribe to RealSense Color & Depth Images
        self.sub_color = self.create_subscription(Image, '/camera/camera/color/image_raw', self.image_callback_color, 10)
        self.sub_depth = self.create_subscription(Image, '/camera/camera/depth/image_rect_raw', self.image_callback_depth, 10)
        self.sub_camera_info = self.create_subscription(CameraInfo, '/camera/camera/color/camera_info', self.camera_info_callback, 10)

        # Publish Target 3D Location & Target Category
        self.pub_target_position = self.create_publisher(TargetBlock, "/robot/target_position", 10)

        # Initializing the OpenCV Bridge
        self.bridge = CvBridge()

        # Loading YOLOv8 Models
        self.model = YOLO("best_copy.pt")

        # Store recent RGB & Depth images
        self.color_image = None
        self.depth_image = None

        # Initialize Camera Internal Reference
        self.fx, self.fy = None, None
        self.cx, self.cy = None, None

        self.get_logger().info("YOLOv8 RealSense Target Detection & Depth Ranging node is up!")

    def camera_info_callback(self, msg):
        """ Get Camera Insider """
        self.fx, self.fy = msg.k[0], msg.k[4]
        self.cx, self.cy = msg.k[2], msg.k[5]
        self.get_logger().info(f"Camera Insider: fx={self.fx}, fy={self.fy}, cx={self.cx}, cy={self.cy}")

    def image_callback_color(self, msg):
        """ Processing color images and running YOLO target detection  """
        self.color_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        frame = self.color_image.copy()

        results = self.model(frame)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get detection box
                class_id = int(box.cls[0])  # Get category index
                conf = float(box.conf[0])  # Getting Confidence

                # Calculate target center point
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                # Get target 3D coordinates
                target_position = self.get_3d_position(center_x, center_y)

                if target_position is not None:
                    X, Y, Z = target_position
                    self.publish_target_position(X, Y, Z, class_id)

                    # Plotting detection frames and depth information
                    label = f"{self.model.names[class_id]} {conf:.2f} - {Z:.2f}m"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (255, 255, 255), 2)

        # Display of test results
        cv2.imshow("YOLOv8 RealSense Detection", frame)
        cv2.waitKey(1)

    def image_callback_depth(self, msg):
        """ Processing depth images  """
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, "16UC1")  # 16-bit depth picture

    def get_3d_position(self, x, y):
        """ Get the 3D world coordinates of the target (X, Y, Z) """
        if self.depth_image is None or self.fx is None:
            return None  # No in-depth data or in-camera references

        # Get depth map size
        depth_h, depth_w = self.depth_image.shape

        # Get RGB image size
        rgb_h, rgb_w, _ = self.color_image.shape

        # Calculating scaling
        scale_x = depth_w / rgb_w
        scale_y = depth_h / rgb_h

        # Calculate the coordinates of the pixels in the depth map
        depth_x = int(x * scale_x)
        depth_y = int(y * scale_y)

        # Make sure the coordinates are in range
        depth_x = np.clip(depth_x, 0, depth_w - 1)
        depth_y = np.clip(depth_y, 0, depth_h - 1)

        # Read depth value
        depth_value = self.depth_image[depth_y, depth_x]

        # Processing invalid depth values
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
                print("Still no valid depth, return None")
                return None
        # if depth_value == 0:
        #     return None

        # Calculating 3D world coordinates
        Z = depth_value / 1000.0  # mm Convert to meters
        X = (x - self.cx) * Z / self.fx
        Y = (y - self.cy) * Z / self.fy

        return (X, Y, Z)


    def publish_target_position(self, X, Y, Z, class_id):
        """ Publish target location & color, bound to a message at the same time """
        
        """class_id names:
        0 - blue block
        1 - yellow block
        2 - green block
        3 - purple block
        4 - red block
        5 - orange block
        6 - blue bin
        7 - purple bin
        8 - green bin
        I will add more code to distinguish bins and blocks
        """"

        
        if Z < 0:
            return  # Depth ineffective. Skip.

        # Setting the target type
        if class_id < 6:
            target_msg.type = "block"
        else:
            target_msg.type = "bin"
        

        # Creating a TargetBlock Message
        target_msg = TargetBlock()

        # Setting the target position
        target_msg.position.header.stamp = self.get_clock().now().to_msg()
        target_msg.position.pose.position.x = X
        target_msg.position.pose.position.y = Y
        target_msg.position.pose.position.z = Z

        # Setting the target color
        target_msg.color = self.model.names[class_id].split(" ")[0]
        # target_msg.color = self.model.names[class_id]

        # Post a message
        self.pub_target_position.publish(target_msg)

        self.get_logger().info(f"📍 Target: {target_msg.color}, Position: (X={X:.2f}, Y={Y:.2f}, Z={Z:.2f})")


def main(args=None):
    rclpy.init(args=args)
    node = YOLOv8RealSenseNode()
    rclpy.spin(node)
    node.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
