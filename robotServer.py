from Robot4WD.Robot4WD import RobotControl
from SimpleUDP.SimpleUDPServer import SimpleUDPServer

import time

# from numpy import interp



UDP_IP = "" ## Accept all IPs
UDP_PORT = 5005

server = SimpleUDPServer(UDP_IP, UDP_PORT)

LEFT_TRIM = 0
RIGHT_TRIM = 0

# robot = Robot4WD(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM, left_id1=1, right_id1=2, left_id2=3, right_id2=4)
robot = RobotControl()
while True:

    inputs = server.listen()

    axis_speed = inputs['axis'][5]
    axis_steering = inputs['axis'][2]
    axis_pan = inputs['axis'][0]
    axis_tilt = inputs['axis'][1]
    hat_x = inputs['axis'][0]
    hat_y = inputs['axis'][1]

    robot.update(axis_speed, axis_steering)

    # time.sleep(0.001)

