from math import pi, cos, sin, asin

import RPi.GPIO as GPIO

from consts import R_BIG_WHEEL_DIAMETER, ENCODER_GEAR_NUMBER_OF_TEETH, R_BIG_WHEELS_CENTERS_DISTANCE

TEETH_S = 2 * pi * R_BIG_WHEEL_DIAMETER / 2 / ENCODER_GEAR_NUMBER_OF_TEETH # odlebłość na jeden ząb
ANGLE_RESOLUTION = TEETH_S/R_BIG_WHEELS_CENTERS_DISTANCE
ANGLE_CHANGE = asin(ANGLE_RESOLUTION)

class Wheel:
    def __init__(self, gpio_pin):
        GPIO.setup(gpio_pin, GPIO.IN)
        self.gpio = gpio_pin
        self.s = 0
        self.encoder_states_history = []
        self.x = [0]
        self.y = [0]
        self.state_changes = 0

    def update(self, angle):
        state = GPIO.input(self.gpio)
        angle_change = 0
        if len(self.encoder_states_history) > 0:
            if self.encoder_states_history[-1] == 1 and state == 0:
                self.state_changes += 1
                self.s += TEETH_S
                self.x.append(self.x[-1] + TEETH_S * cos(angle * pi / 180))
                self.y.append(self.y[-1] + TEETH_S * sin(angle * pi / 180))
                angle_change = ANGLE_CHANGE
        self.encoder_states_history.append(state)
        return angle_change

class Encoder:
    def __init__(self, left_wheel_gpio, right_wheel_gpio):
        GPIO.setmode(GPIO.BCM) # should be probably done globally in main.py
        self.left_wheel = Wheel(left_wheel_gpio)
        self.right_wheel = Wheel(right_wheel_gpio)
        self.current_angle = 0  # degrees
        self.angle_history = [0]

    def update_angle(self, left_wheel_part, right_wheel_part):
        self.current_angle += left_wheel_part - right_wheel_part
        if self.angle_history[-1] != self.current_angle:
            self.angle_history.append(self.current_angle)

    def update(self):
        left_wheel_angle_change = self.left_wheel.update(self.current_angle)
        right_wheel_angle_change = self.right_wheel.update(self.current_angle)
        self.update_angle(left_wheel_angle_change, right_wheel_angle_change)

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
    enkoder = Encoder()