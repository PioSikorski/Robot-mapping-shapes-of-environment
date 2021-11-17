#!/usr/bin/python3
import RPi.GPIO as GPIO
from motor import Motor
import curses
import time
from imu import Imu
import keyboard

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.setwarnings(False)

motor_left = Motor(14, 15, 18)
motor_right = Motor(25,8,7)

class Move():

    def movF():
        motor_right.moveF()
        motor_left.moveF()

    def movB():
        motor_right.moveB()
        motor_left.moveB()

    def movL():
        motor_right.moveF()

    def movR():
        motor_left.moveF()

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

def handle_imu(angle, imu):
    d_angle = imu.get_angle_change()
    if d_angle is not None:
        angle += d_angle
        if angle > 360:
            angle -= 360
        if angle < -360:
            angle += 360
        print(angle)
    return angle

if __name__=="__main__":
    try:
        imu = Imu('y')
        imu.calibrate()
        angle = 0
        add_hook_keyboard()

        while True:
            handle_imu(angle, imu)
            move_on_click()

            
    except KeyboardInterrupt:
        motor_left.stop()
        motor_right.stop()

    finally:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()

    