from math import pi, cos, sin, asin
import RPi.GPIO as GPIO
import time

from imu import Imu
from control import Move
from control import handle_imu
from consts import R_BIG_WHEEL_DIAMETER, ENCODER_GEAR_NUMBER_OF_TEETH, R_BIG_WHEELS_CENTERS_DISTANCE

distance_per_rotation = 2 * pi * R_BIG_WHEEL_DIAMETER / 2 / ENCODER_GEAR_NUMBER_OF_TEETH # odlebłość na jeden ząb


class Wheel:
    def __init__(self, GPIO_PIN):
        GPIO.setup(GPIO_PIN, GPIO.IN)
        self.gpio = GPIO_PIN
        self.s = 0
        self.encoder_states_history = []
        self.x = [0]
        self.y = [0]
        self.state_changes = 0

    def update(self, angle):
        state = GPIO.input(self.gpio)
        if len(self.encoder_states_history) > 0:
            if self.encoder_states_history[-1] == 1 and state == 0:
                self.state_changes += 1
                print(f"self.state_changes {self.state_changes}")
                self.s += distance_per_rotation
                self.x.append(self.x[-1] + distance_per_rotation * cos(angle * pi / 180))
                self.y.append(self.y[-1] + distance_per_rotation * sin(angle * pi / 180))
        self.encoder_states_history.append(state)
        return angle

class Encoder:
    def __init__(self, left_wheel_gpio, right_wheel_gpio):
        GPIO.setmode(GPIO.BCM) # should be probably done globally in main.py
        self.left_wheel = Wheel(left_wheel_gpio)
        self.right_wheel = Wheel(right_wheel_gpio)
        self.current_angle = 0  # degrees
        self.angle_history = [0]

    def update(self, angle):
        self.left_wheel.update(angle)
        self.right_wheel.update(angle)

    def show_state(self):
        print(self.left_wheel.s, self.right_wheel.s)

    def store_details(self):
        with open('encoder_path_left_wheel.txt', 'w') as f1:
            for x, y in zip(self.left_wheel.x, self.left_wheel.y):
                f1.writelines(f'{x}, {y} \n')
            f1.close()
        with open('encoder_path_right_wheel.txt', 'w') as f2:
            for x, y in zip(self.right_wheel.x, self.right_wheel.y):
                f2.writelines(f'{x}, {y} \n')
            f2.close()

if __name__=="__main__":
    left_encorer_sensor_gpio_pin_number = 19
    right_encorer_sensor_gpio_pin_number = 26
    enkoder = Encoder(left_encorer_sensor_gpio_pin_number, right_encorer_sensor_gpio_pin_number)
