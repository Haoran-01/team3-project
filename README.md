# team3-project

## Clone this project
```bash git clone https://github.com/Haoran-01/team3-project.git```


## Run object detection
- First connect the camera
- Second run the camera: ```ros2 launch realsense2_camera rs_launch.py depth_module.profile:=1280x720x120 pointcloud.enable:=true align_depth:=true```
- Third run the object_detection_final.py by using the terminal ```python3 object_detection_final.py```