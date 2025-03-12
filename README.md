# team3-project

## Introduction
This project is designed for 

## Clone this project

First, clone the repository from GitHub using the following command:

 ```bash
 git clone https://github.com/Haoran-01/team3-project.git
 ```

Then, navigate to the project root directory:

```bash
cd team3-project
```

## Create a new virtual environment
To prevent dependency conflicts, create a Python virtual environment:

```bash
python3 -m venv team3-project
```

Activate the virtual environment:

```bash
source team3-project/bin/activate
```

After activation, your terminal should display `(team3-project) user@linux:~/your_project$`, indicating that the environment is active.

## Install the dependencies
Before running the code, install all required dependencies:

```bash
pip install -r requirements.txt
```

## Build you ROS2 workplace
Once dependencies are installed, build your ROS2 workspace:

```bash
colcon build
source install/setup.bash
```

If you encounter build errors, ensure:

- ROS2 is installed correctly.
- You have sourced the ROS2 environment (`source /opt/ros/<your_ros2_distribution>/setup.bash`).



## Run Object Detection

### Step 1: Connect the Camera

Make sure your **Intel RealSense camera** is properly connected to your system.

### Step 2: Launch the Camera

Run the following command to start the RealSense camera:

```bash
ros2 launch realsense2_camera rs_launch.py depth_module.profile:=1280x720x120 pointcloud.enable:=true align_depth:=true
```

### Step 3: Run Object Detection Script

Once the camera is running, execute the object detection script:

```bash
python3 object_detection_final.py
```

If you encounter issues:

- Check if the camera is recognized using `lsusb` (Linux) or `realsense-viewer`.
- Ensure the ROS2 package `realsense2_camera` is correctly installed.

## Output the `requirements.txt` File

If you have installed new dependencies and need to update `requirements.txt`, use:

```bash
pip freeze > requirements.txt
```

## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.
