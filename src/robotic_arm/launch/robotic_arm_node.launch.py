from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            output='screen',
            emulate_tty=True,
            package='robotic_arm',
            executable='px100_pick_and_place',
            name='px100_pick_and_place_node',
            parameters=[{
                "z_min": 0.02,
                "z_max": 0.25,
                "r_min": 0.05,
                "r_max": 0.3,
                "place_positions": {
                    "blue": [0.2, 0.2, 0.1],
                    "yellow": [0.1, 0.2, 0.1],
                    "green": [0.2, 0.1, 0.1]
                }
            }]
        )
    ])

