# team3-project

## Clone this project
```git clone https://github.com/Haoran-01/team3-project.git```

```cd team3-project.git```

## Create a new virtual environment
```python3 -m venv team3-project```

Before using the project each time, you need to activate the virtual environment using following code in the terminal
```source venv/bin/activate```
After activate the virtual environment you will see you terminal like: (team3-project) user@linux:~/your_project$

## Install the dependencies
```pip install -r requirements.txt```

## Build you ROS2 workplace
```colcon build```

```source install/setup.bash```

## Run object detection
- First connect the camera
- Second run the camera: ```ros2 launch realsense2_camera rs_launch.py depth_module.profile:=1280x720x120 pointcloud.enable:=true align_depth:=true```
- Third run the object_detection_final.py by using the terminal ```python3 object_detection_final.py```