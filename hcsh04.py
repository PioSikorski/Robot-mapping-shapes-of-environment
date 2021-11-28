import time

import RPi.GPIO as GPIO


SOUND_SPEED = 343000
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
        while GPIO.input(self.echo) == 0:
            if (time.time() - trigger_time) > MAX_TIME_TO_RETURN:
                return 10000000 # infinity
            print(self.trig, 0)
        while GPIO.input(self.echo) == 1:
            print(self.trig, 1)
            stop_time = time.time()
        time_dist = stop_time - trigger_time
        distance = (time_dist * SOUND_SPEED) / 2
        return distance
