import time

import RPi.GPIO as GPIO

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

    def measure(self):
    
        GPIO.output(self.trig, True) # set Trigger to HIGH
 
        time.sleep(0.00001) # set Trigger after 0.01ms to LOW
        GPIO.output(self.trig, False)
        trigger_time = time.time()
        StartTime = time.time()
        StopTime = time.time()
 
        while GPIO.input(self.echo) == 0:
            StartTime = time.time() # save StartTime
            if (time.time() - trigger_time) > MAX_TIME_TO_RETURN:
                return 100000
        while GPIO.input(self.echo) == 1:
            StopTime = time.time() # save time of arrival
 
        TimeElapsed = StopTime - StartTime # time difference between start and arrival
        distance = (TimeElapsed * 34300) / 2 # multiply with the sonic speed (34300 cm/s) and divide by 2
 
        return distance

if __name__ == "__main__":
    try:
        left_dist_sensor = DistanceSensor(6, 13)
        middle_dist_sensor = DistanceSensor(5, 0)
        right_dist_sensor = DistanceSensor(11, 9)
        while True:
            print(left_dist_sensor.measure())
            print(middle_dist_sensor.measure())
            print(right_dist_sensor.measure())
            time.sleep(0.5)
    except KeyboardInterrupt:
        exit()
        GPIO.cleanup()