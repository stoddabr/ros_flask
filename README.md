# About

Simple Flask - ROS prototype.

Alternative to using [ROSLIBJS](http://wiki.ros.org/roslibjs)

Send motion commands via `http://localhost:5000/send_movement_command/<direction>`

View possible commands at `http://localhost:5000/help`

An in-depth tutorial is available on the [ros_flask wiki](https://github.com/stoddabr/ros_flask/wiki/Tutorial)

# Basic Quickstart

After setting up ROS catkin and making, run this:
```bash
roslaunch flask_ros start_server.launch
```

For more information view the flask_ask_ros repo linked below.

# Limitations

* Flask HTML templates don't seem to work.
See /src/html.py for used workaround for providing html responses.
This could be an issue with how ROS manages directories.

# Acknowledgements

originally cloned from this repo by the [3Spheres Project](https://3srp.com/):
  https://github.com/3SpheresRoboticsProject/flask_ask_ros

found from this article which explains why this works:
  https://campus-rover.gitbook.io/lab-notebook/cr-package/web-application/flask-and-ros

for use in Oregon State University's Charisma Lab:
  https://www.charismarobotics.com/
