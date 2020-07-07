# About

Simple Flask - ROS prototype

Send motion commands via
`/send_movement_command/<direction>`

View possible commands at  
`http://localhost:5000/help`

# Quickstart

Run this using catkin
`roslaunch flask_ask_ros start_skill_server.launch`

For more information view the flask_ask_ros repo.

# Limitations

* Flask HTML templates don't seem to work.
See /src/html.py for used workaround for providing html reponses


# Acknoledgements

originally cloned from this repo:
  https://github.com/3SpheresRoboticsProject/flask_ask_ros

found from this article:
  https://campus-rover.gitbook.io/lab-notebook/cr-package/web-application/flask-and-ros

for use in Oregon State University's Charisma Lab:
  https://www.charismarobotics.com/
