#!/usr/bin/env python
import os
import rospy
import threading

from flask import Flask
from flask_ask import Ask, question, statement
from std_msgs.msg import String

app = Flask(__name__)
ask = Ask(app, "/")

# ROS node, publisher, and parameter.
# The node is started in a separate thread to avoid conflicts with Flask.
# The parameter *disable_signals* must be set if node is not initialized
# in the main thread.

threading.Thread(target=lambda: rospy.init_node('test_node', disable_signals=True)).start()
pub = rospy.Publisher('test_pub', String, queue_size=1)
NGROK = rospy.get_param('/ngrok', None)


@ask.launch
def launch():
    '''
    Executed when launching skill: say "Alexa, ask tester"
    '''
    welcome_sentence = 'Hello, this is a test skill. Please state a command.'
    return question(welcome_sentence)


@ask.intent('FirstName', default={'name': None})
def test_intent_function(name):
    '''
    Executed when "FirstName" is called:
    say "Alexa, ask tester to say (first name of a person)"
    Note that the 'intent_name' argument of the decorator @ask.intent
    must match the name of the intent in the Alexa skill.
    '''
    pub.publish(name)
    return statement('I have published the following name to a ROS topic: {0}.'.format(name))


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if NGROK:
        print 'NGROK mode'
        app.run(port=5000)
    else:
        print 'Manual tunneling mode'
        dirpath = os.path.dirname(__file__)
        cert_file = os.path.join(dirpath, '../config/ssl_keys/certificate.pem')
        pkey_file = os.path.join(dirpath, '../config/ssl_keys/private-key.pem')
        app.run(host=your_ip_or_hostname, port=5000,
                ssl_context=(cert_file, pkey_file))
    
