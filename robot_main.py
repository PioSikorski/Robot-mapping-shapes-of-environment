import csv
import socket
import threading
import time

import RPi.GPIO as GPIO

from consts import PI_IP_ADDRESS, SERVER_PORT, LEFT_ENCODER_SENSOR_PIN, RIGHT_ENCODER_SENSOR_PIN, LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE, MIDDLE_SENSOR_DISTANCE_FROM_ROBOT_CENTRE, RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE, DEBUG
from enkoder import Encoder
from hcsh04 import DistanceSensor
from imu import Imu
from server import Server


GPIO.setwarnings(False)

if __name__ == "__main__":
    measures = []
    try:
        # sensors should be initialized before operator is able to move robot
        imu = Imu('y')
        imu.calibrate()

        enkoder = Encoder(LEFT_ENCODER_SENSOR_PIN, RIGHT_ENCODER_SENSOR_PIN)

        left_dist_sensor = DistanceSensor(6, 13)
        middle_dist_sensor = DistanceSensor(5, 0)
        right_dist_sensor = DistanceSensor(11, 9)

        server = Server()
        server.serve()

        x = 0

        while True:
            print('a')
            imu.update_angle()
            print('b')
            enkoder.update(imu.angle)
            print('c')
            print(x)
            if x % 50 == 0:
                print('append')
                measures.append(
                    [
                        (enkoder.left_wheel.x[-1] + enkoder.right_wheel.x[-1])/2,
                        (enkoder.left_wheel.y[-1] + enkoder.right_wheel.y[-1])/2,
                        imu.angle,
                        left_dist_sensor.measure() + LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE,
                        middle_dist_sensor.measure() + MIDDLE_SENSOR_DISTANCE_FROM_ROBOT_CENTRE,
                        right_dist_sensor.measure() + RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE
                    ]
                )
            if x % 500 == 0:
                print(x)
                enkoder.show_state()
            x += 1

    except KeyboardInterrupt:
        server.stop_serving()
        GPIO.cleanup()
        if measures:
            with open('res.csv', 'w', newline='') as f:
                print('Zapisywanie')
                l = len(measures)
                w = csv.writer(f)
                w.writerow(['robot_x', 'robot_y', 'angle', 'left', 'middle', 'right'])
                for i, measure in enumerate(measures):
                    w.writerow(measure)
                    print(f'{i}/{l} written')
        else:
            print('nie ma')


