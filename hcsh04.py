import time
from math import cos, pi, sin

import RPi.GPIO as GPIO

from consts import SENSORS_ANGLE


# print('Pomiar odleglosci')


# SENSORS = {"LEFT":{"echo":6,"trig":13},
#            "MIDDLE":{"echo":5,"trig":0},
#            "RIGHT":{"echo":11,"trig":9}}


# for k,v in SENSORS.items():
#     GPIO.setup(v["trig"], GPIO.OUT)
#     GPIO.setup(v["echo"], GPIO.IN)

# measurment = []
# result = {"LEFT":[],
#           "MIDDLE":[],
#           "RIGHT":[]}

# def distance():
#     for k,v in SENSORS.items():
#         GPIO.output(v['trig'], True)
#         time.sleep(0.00001)
#         GPIO.output(v['trig'], False)
#         while GPIO.input(v['echo']) == 0:
#             #print(v['echo'], 0)
#             start_time = time.time()

#         while GPIO.input(v['echo']) == 1:
#             #print(v['echo'], 1)
#             stop_time = time.time()
#         time_dist = stop_time - start_time
#         distance = (time_dist * 34300) / 2
#         print(k, distance)
#         result[k].append(distance)

#     time.sleep(0.5)
#     return result

# def write_result():
#     for k, v in result.items():
#         with open(f"{k}_result_file.txt", 'w') as f:
#             for el in v:
#                 f.write(str(el) + "\n")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class DistanceSensor:
    def __init__(self, gpio_echo_pin, gpio_trig_pin):
        self.echo = gpio_echo_pin
        self.trig = gpio_trig_pin
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def measure(self) -> float:
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        while GPIO.input(self.echo) == 0:
            start_time = time.time()
        while GPIO.input(self.echo) == 1:
            stop_time = time.time()
        time_dist = stop_time - start_time
        distance = (time_dist * 34300) / 2
        return distance

# if __name__ == '__main__':
#     try:
#         while True:
#             dist = distance()
#             print(dist)

#     except KeyboardInterrupt:
#         print('Stop klawiatura')
#         write_result()
#         GPIO.cleanup()
