import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

class Motor():

    def __init__(self,Ena,In1,In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)

        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(0)

    def moveF(self,x=18):
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        self.pwm.ChangeDutyCycle(x)

    def moveB(self,x=18):
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        self.pwm.ChangeDutyCycle(x)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)

if __name__=="__main__":
    try:
        motor_left = Motor(14, 15, 18)
        motor_right = Motor(25,8,7)

        motor_left.moveF()
        motor_right.moveF()
        time.sleep(5)
        motor_left.stop()
        motor_right.stop()

    except KeyboardInterrupt:
        motor_left.stop()
        motor_right.stop()