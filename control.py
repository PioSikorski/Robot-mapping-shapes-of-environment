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
#GPIO.setwarnings(False)

# motor_right = Motor(14, 15, 18)
# motor_left = Motor(25,8,7)


class Move():
    def initialize_motors():
        motor_left = Motor(25, 8, 7)
        motor_right = Motor(14, 15, 18)

    def movF():
        motor_right.moveF()
        motor_left.moveF()

    def movB():
        motor_right.moveB()
        motor_left.moveB()

    def movL():
        motor_right.moveF()
        motor_left.stop()

    def movR():
        motor_left.moveF()
        motor_right.stop()

    def stop():
        motor_right.stop()
        motor_left.stop()


def add_hook_keyboard():
    keyboard.on_press_key("w", Move.movF)
    keyboard.on_press_key("s", Move.movB)
    keyboard.on_press_key("d", Move.movR)
    keyboard.on_press_key("a", Move.movL)


def move_on_click():
    char = screen.getch()
    if char == curses.KEY_UP:
        Move.movF()
    elif char == curses.KEY_DOWN:
        Move.movB()
    elif char == curses.KEY_RIGHT:
        Move.movR()
    elif char == curses.KEY_LEFT:
        Move.movL()


def move_on_click2():
    if keyboard.is_pressed("w"):
        Move.movF()
    elif keyboard.is_pressed("s"):
        Move.movB()
    elif keyboard.is_pressed("d"):
        Move.movR()
    elif keyboard.is_pressed("a"):
        Move.movL()


if __name__ == "__main__":
    try:
        imu = imu.Imu('y')
        imu.calibrate()
        angle = 0
        add_hook_keyboard()

        while True:
            imu.handle_imu()
            add_hook_keyboard()

    except KeyboardInterrupt:
        motor_left.stop()
        motor_right.stop()

    finally:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
