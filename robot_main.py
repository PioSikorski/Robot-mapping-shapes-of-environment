import csv
import socket
import threading
import time

from consts import PI_IP_ADDRESS, SERVER_PORT, LEFT_ENCODER_SENSOR_PIN, RIGHT_ENCODER_SENSOR_PIN
from enkoder import Encoder
from imu import Imu
from points import Point, get_midpoint
from server import Server
from hcsh04 import DistanceSensor

if __name__ == "__main__":
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
        measures = []

        while True:
            imu.update_angle()
            enkoder.update(imu.angle)

            # measures.append(
            #     {
            #         "robot_x": (enkoder.left_wheel.x[-1] + enkoder.right_wheel.x[-1])/2,
            #         "robot_y": (enkoder.left_wheel.y[-1] + enkoder.right_wheel.y[-1])/2,
            #         "left": left_dist_sensor.measure(),
            #         "middle": middle_dist_sensor.measure(),
            #         "right": right_dist_sensor.measure()
            #     }
            # )
            measures.append(
                [
                    (enkoder.left_wheel.x[-1] + enkoder.right_wheel.x[-1])/2,
                    (enkoder.left_wheel.y[-1] + enkoder.right_wheel.y[-1])/2,
                    left_dist_sensor.measure(),
                    middle_dist_sensor.measure(),
                    right_dist_sensor.measure()
                ]
            )
            if x % 500 == 0:
                enkoder.show_state()
            x += 1

    except KeyboardInterrupt:
        with open('res.csv', 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['robot_x', 'robot_y', 'left', 'middle', 'right'])
            for measure in measures:
                w.writerow(measure)
                
        #enkoder.store_details()
        server.stop_serving()
