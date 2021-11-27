import RPi.GPIO as GPIO
import time
from math import sin, cos, pi

from consts import SENSORS_ANGLE


print('Pomiar odleglosci')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

SENSORS = {"LEFT":{"echo":6,"trig":13},
           "MIDDLE":{"echo":5,"trig":0},
           "RIGHT":{"echo":11,"trig":9}}


for k,v in SENSORS.items():
    GPIO.setup(v["trig"], GPIO.OUT)
    GPIO.setup(v["echo"], GPIO.IN)

measurment = []
result = {"LEFT":[],
          "MIDDLE":[],
          "RIGHT":[]}
             
<<<<<<< HEAD
def distance():
=======
def distance(): 
>>>>>>> fe7c0bd954bbba2141a855fa1722d1a40e124dfa
    for k,v in SENSORS.items():
        GPIO.output(v['trig'], True)
        time.sleep(0.00001)
        GPIO.output(v['trig'], False)
        while GPIO.input(v['echo']) == 0:
            #print(v['echo'], 0)
            start_time = time.time()

        while GPIO.input(v['echo']) == 1:
            #print(v['echo'], 1)
            stop_time = time.time()
        time_dist = stop_time - start_time
        distance = (time_dist * 34300) / 2
        print(k, distance)
        result[k].append(distance)
        
    time.sleep(0.5)        
    return result

<<<<<<< HEAD
def write_result():
    for k, v in result.items():
=======

def write_result():
    for k,v in result.items():
>>>>>>> fe7c0bd954bbba2141a855fa1722d1a40e124dfa
        with open(f"{k}_result_file.txt", 'w') as f:
            for el in v:
                f.write(str(el) + "\n")
    

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print(dist)
            handle_data()
                
    except KeyboardInterrupt:
        print('Stop klawiatura')
        write_result()
        GPIO.cleanup()