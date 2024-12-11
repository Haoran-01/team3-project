from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch_ros.actions import Node, SetParameter
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import xacro
import os

def generate_launch_description():#
    ld = LaunchDescription()
    # IMU Node
    imu_node = Node(
        package='imu',  # 替换为 IMU 节点所在的包名
        executable='imu_node',  # 替换为 IMU 节点的可执行文件名
        name='imu_node',
        output='screen'
    )

    # NUC Node (Task Coordinator)
    nuc_node = Node(
        package='nuc',  # 替换为 NUC 节点所在的包名
        executable='nuc_node',  # 替换为 NUC 节点的可执行文件名
        name='nuc_node',
        output='screen'
    )

    # Arm Node
    robotic_arm_node = Node(
        package='robotic_arm',  # 替换为 Arm 节点所在的包名
        executable='robotic_arm_node',  # 替换为 Arm 节点的可执行文件名
        name='arm_node',
        output='screen'
    )

    # Lidar Node
    lidar_node = Node(
        package='lidar',  # 替换为 Lidar 节点所在的包名
        executable='lidar_node',  # 替换为 Lidar 节点的可执行文件名
        name='lidar_node',
        output='screen'
    )

    # Camera Node
    camera_node = Node(
        package='camera',  # 替换为 Camera 节点所在的包名
        executable='camera_node',  # 替换为 Camera 节点的可执行文件名
        name='camera_node',
        output='screen'
    )

    # Navigation Node
    nav_node = Node(
        package='navigation',  # 替换为 Navigation 节点所在的包名
        executable='navigation_node',  # 替换为 Navigation 节点的可执行文件名
        name='navigation_node',
        output='screen'
    )

    # # Start SLAM Toolbox with default parameters
    # launch_slam_toolbox = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(
    #         get_package_share_directory('slam_toolbox'), 'launch'),
    #         '/online_async_launch.py'])
    # )

    leo_rover_node = Node(
        package='leo_rover',  # 替换为 Navigation 节点所在的包名
        executable='leo_rover_node',  # 替换为 Navigation 节点的可执行文件名
        name='leo_rover_node',
        output='screen'
    )

    controller_server_node = Node(
        package='controller_server',
        executable='controller_server_node',
        name='controller_server_node',
        output='screen'
    )

    pkg_name = 'nuc'
    slam_file_path = "/config/slam_toolbox.yaml"
    full_slam_file_path = os.path.join(get_package_share_directory(pkg_name), slam_file_path)

    launch_slam_toolbox = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',  # 或 sync_slam_toolbox_node
        name='slam_toolbox',
        parameters=[full_slam_file_path],
        output='screen'
    )

    data_integration_node = Node(
        package='data_integration',
        executable='data_integration_node',
        name='data_integration',
        output='screen'
    )


    ld.add_action(imu_node)
    ld.add_action(nuc_node)
    ld.add_action(robotic_arm_node)
    ld.add_action(lidar_node)
    ld.add_action(camera_node)
    ld.add_action(leo_rover_node)
    ld.add_action(controller_server_node)
    ld.add_action(data_integration_node)
    ld.add_action(nav_node)
    ld.add_action(launch_slam_toolbox)
    return ld