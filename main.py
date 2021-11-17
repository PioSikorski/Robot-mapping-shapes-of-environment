import time

from motor import Motor
from enkoder import Encoder, Wheel


def print_wheel_points(wheel_object: Wheel):
    for x, y in zip(wheel_object.x, wheel_object.y):
        print(f'[{x}; {y}]')
    print(wheel_object.state_changes)

if __name__=="__main__":
    left_encorer_sensor_gpio_pin_number = 19
    right_encorer_sensor_gpio_pin_number = 26
    try:
        enkoder = Encoder(left_encorer_sensor_gpio_pin_number, right_encorer_sensor_gpio_pin_number)
        # run robot
        left_motor = Motor(14, 15, 18)
        right_motor = Motor(25, 8, 7)
        left_motor.moveF()
        right_motor.moveF()
        # gather data from encoder
        start = time.time()
        while time.time() - start < 3:
            enkoder.update() 
        # stop motor
        left_motor.stop()
        right_motor.stop()
        # get points
        print('left wheel:')
        print_wheel_points(enkoder.left_wheel)
        print('right wheel:')
        print_wheel_points(enkoder.right_wheel)
        enkoder.store_details()
        print(enkoder.angle_history)

    except KeyboardInterrupt:
        left_motor.stop()
        right_motor.stop()