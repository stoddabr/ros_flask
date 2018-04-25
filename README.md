# flask_ask_ros
A locally hosted web service + ROS node for custom Alexa skills based on [Flask-Ask](https://github.com/johnwheeler/flask-ask).

## Table of Contents

* [Description](README.md#description)
* [Requirements](README.md#requirements)
* [Maintainers](README.md#maintainers)
* [Installation](README.md#installation)
* [Usage](README.md#usage)
* [TO DO](README.md#todo)

## Description
This package combines a Flask server and ROS node into a script that serves as an endpoint for a custom Alexa Skill. This enables information sent by voice to the Amazon Alexa to be processed by other ROS nodes and services.

In this package we provide a simple Alexa skill that parses a single slot (word/argument) from an utterance (spoken function call) and publishes it to a ROS topic. 


## Requirements

* Ubuntu 16.04

* ROS Kinetic

* Flask-ask (Python): follow installation from source [here.](https://github.com/johnwheeler/flask-ask/blob/master/README.rst#development)

## Maintainers

* Lucas Porto <lucasporto@outlook.com>

* Sina Radmard <s.radmard85@gmail.com>

## Installation

* Navigate to source directory of your ROS catkin workspace (e.g. `catkin_ws`):

  ``` bash
      cd catkin_ws/src
      git clone https://github.com/3SpheresRoboticsProject/flask_ask_ros
  ```

* Build catkin workspace:

  ``` bash
      cd catkin_ws
      catkin_make
  ```

* If necessary, set script file permissions to executable:

  ``` bash
      chmod +x catkin_ws/src/flask_ask_ros/src/*
  ```

* Source workspace:

  ``` bash
      source catkin_ws/devel/setup.bash
  ```

## Usage

### Endpoint configuration

In order for the Alexa requests to reach the local skill server, the local network must be configured to tunnel HTTPS traffic to a specific port on the local machine.

We have tested two ways to accomplish this:

* Using ngrok as a tunnel

* Static IP/Dynamic DNS + self-signed SSL certificate

### ngrok tunnel configuration

1. Set the `ROS_IP` environment variable to be the local machine IP

2. Download [ngrok for Linux](https://ngrok.com/download) and unzip

3. Start an ngrok server:
   
   ``` bash
   ./ngrok http $ROS_IP:5000
   ```
4. Open the [Amazon Developer Console](https://developer.amazon.com/alexa/console/ask) and navigate to your custom skill:
   
   * Under *Configuration*, select *HTTPS* and paste the URL shown on the ngrok terminal (see below).
	 
	 ![alt text][ngrok_url]
   
   * Under *SSL Certificate* select *My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority.*

5. Run the skill server with the ngrok argument set to `true`:
   
   ``` bash
   roslaunch flask_ask_ros start_skill_server.launch ngrok:=true
   ```

[ngrok_url]: https://github.com/3SpheresRoboticsProject/flask_ask_ros/raw/master/common/ngrok.png "ngrok terminal"

### Static IP/Dynamic DNS + self-signed SSL certificate

1. Set the `ROS_IP` environment variable to be the local machine IP

2. Configure the router to forward HTTPS requests (port 443) from the local network's public IP to a local IP and port 5000

   This setting is usually located under 'Virtual Server', or 'Port triggering'. See an example below on the D-Link DIR-655 router.

   ![alt_text][virt_srv]

3. Include the static IP and/or Dynamic DNS hostname in a SSL configuration file `/config/ssl_keys/configuration.cnf` (sample provided)

   Under `[subject_alternate_names]` add the line `IP.1 = <your ip>` and/or `DNS.1 = <your hostname>`

4. Run the script `generate_ssl_cert.sh` to generate the certificate in `/config/ssl_keys/certificate.pem`

5. Open the [Amazon Developer Console](https://developer.amazon.com/alexa/console/ask) and navigate to your custom skill:

   * Under *Configuration*, select *HTTPS* and type in `https://<your hostname>` or `https://<your ip>`

   * Under *SSL Certificate*, select *I will upload a self-signed certificate...* and paste the contents of `/config/ssl_keys/certificate.pem`

6. Run the skill server
   
   ``` bash
   roslaunch flask_ask_ros start_skill_server.launch
   ```

[virt_srv]: https://github.com/3SpheresRoboticsProject/flask_ask_ros/raw/master/common/virt_serv.png "D-Link DIR-655 Virtual Server setting example"


## Testing

In order to test the provided skill server, open your [Amazon Developer Console](https://developer.amazon.com/alexa/console/ask), create a custom skill, and follow the [steps above to configure your endpoint](README.md#Usage).

Inside the skill builder, navigate to the *JSON Editor* and paste the contents of `src/test_skill.json`. Save and build the model.

Run the skill server to test your skill.

## TODO

* Sample code for ROS services

This app was not created or endorsed by Amazon.
