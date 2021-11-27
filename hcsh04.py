import time

import RPi.GPIO as GPIO


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
