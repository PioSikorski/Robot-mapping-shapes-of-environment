#!/usr/bin/python3
import RPi.GPIO as GPIO
from motor import Motor
import curses
import time
import imu
import keyboard

# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)
# GPIO.setwarnings(False)

# self.motor_right = Motor(14, 15, 18)
# self.motor_left = Motor(25,8,7)


class Move():
    def __init__(self, left_wheel_params, right_wheel_params):
        self.left_wheel_params = left_wheel_params
        self.right_wheel_params = right_wheel_params
        self.motor_left = None
        self.motor_right = None

    def initialize_motors(self):
        self.motor_left = Motor(*self.left_wheel_params)
        self.motor_right = Motor(*self.right_wheel_params)

    def movF(self):
        self.motor_right.moveF()
        self.motor_left.moveF()

    def movB(self):
        self.motor_right.moveB()
        self.motor_left.moveB()

    def movL(self):
        self.motor_right.moveF()
        self.motor_left.stop()

    def movR(self):
        self.motor_left.moveF()
        self.motor_right.stop()

    def stop(self):
        self.motor_right.stop()
        self.motor_left.stop()


# def add_hook_keyboard():
#     keyboard.on_press_key("w", Move.movF)
#     keyboard.on_press_key("s", Move.movB)
#     keyboard.on_press_key("d", Move.movR)
#     keyboard.on_press_key("a", Move.movL)


# def move_on_click():
#     char = screen.getch()
#     if char == curses.KEY_UP:
#         Move.movF()
#     elif char == curses.KEY_DOWN:
#         Move.movB()
#     elif char == curses.KEY_RIGHT:
#         Move.movR()
#     elif char == curses.KEY_LEFT:
#         Move.movL()


# def move_on_click2():
#     if keyboard.is_pressed("w"):
#         Move.movF()
#     elif keyboard.is_pressed("s"):
#         Move.movB()
#     elif keyboard.is_pressed("d"):
#         Move.movR()
#     elif keyboard.is_pressed("a"):
#         Move.movL()


# if __name__ == "__main__":
#     try:
#         imu = imu.Imu('y')
#         imu.calibrate()
#         angle = 0
#         add_hook_keyboard()

#         while True:
#             imu.handle_imu()
#             add_hook_keyboard()

#     except KeyboardInterrupt:
#         self.motor_left.stop()
#         self.motor_right.stop()

#     finally:
#         curses.nocbreak()
#         screen.keypad(0)
#         curses.echo()
#         curses.endwin()
