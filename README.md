# create2_description

To create a ROS Python package you can use:

```bash
ros2 pkg create --build-type ament_python --node-name driver create2_description
```

## Testing

```bash
ros2 launch create2_description spawn_robot.launch.py use_rviz:=False
```

Inspect frames with:

```bash
ros2 run tf2_tools view_frames.py

xdot frames.gv
```
