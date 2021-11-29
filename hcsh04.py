import time

import RPi.GPIO as GPIO
from consts import LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE, MIDDLE_SENSOR_DISTANCE_FROM_ROBOT_CENTRE, RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE

SOUND_SPEED = 34300
MAX_SENSOR_SUPPORT = 200
MAX_TIME_TO_RETURN = MAX_SENSOR_SUPPORT * 2 / SOUND_SPEED

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
        trigger_time = time.time()
        while True:
            #GPIO.input(self.echo) == 0:
            if (time.time() - trigger_time) > MAX_TIME_TO_RETURN:
                return 100000
            if GPIO.input(self.echo) == 1:
                stop_time = time.time()
                break
        time_dist = stop_time - trigger_time
        distance = (time_dist * SOUND_SPEED) / 2
        return distance

if __name__ == "__main__":
    try:
        left_dist_sensor = DistanceSensor(6, 13)
        middle_dist_sensor = DistanceSensor(5, 0)
        right_dist_sensor = DistanceSensor(11, 9)
        while True:
            print(left_dist_sensor.measure() + LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE)
            print(middle_dist_sensor.measure() + MIDDLE_SENSOR_DISTANCE_FROM_ROBOT_CENTRE)
            print(right_dist_sensor.measure() + RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE)
    except KeyboardInterrupt:
        exit()
        GPIO.cleanup()