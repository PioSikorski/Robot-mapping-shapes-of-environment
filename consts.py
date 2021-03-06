# parameters in m
# cm * 100 = m
# robot consts
R_LENGTH = 17.5 / 100
R_WIDTH = 11 / 100
R_HEIGHT = 7.5 / 100
R_BOX_HEIGHT = 3 / 100
# big wheels are cylinders
R_BIG_WHEEL_DIAMETER = 6.5 / 100
R_BIG_WHEEL_CENTER_FROM_FRONT = 7 / 100
R_BIG_WHEEL_WIDTH = 2.5 / 100
R_BIG_WHEELS_CENTERS_DISTANCE = 10 / 100
R_BIG_WHEELS_AXIS_CENTER_FROM_LEFT = 5.5 / 100  # same as from right
# small wheel is a sphere
R_SMALL_WHEEL_CENTER_FROM_BACK = 2 / 100
R_SMALL_WHEEL_CENTER_FROM_LEFT = 5.5 / 100  # same as from right
R_SMALL_WHEEL_DIAMETER = 1 / 100

ENCODER_GEAR_NUMBER_OF_TEETH = 12


# SERVER
PI_IP_ADDRESS = "192.168.111.17" # raspberry pi IP address
HOST_IP_ADDRESS = "192.168.187.16" # host IP address
SERVER_PORT = 5050

# ENCODER
LEFT_ENCODER_SENSOR_PIN = 19
RIGHT_ENCODER_SENSOR_PIN = 26

#ANGLE BETWEEN SENSORS
LEFT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE = 90  # degrees
MIDDLE_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE = 0  # degrees
RIGHT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE = -90  # degrees

# DISTANCE FROM CENTER TO SENSOR
LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_X = 4 # in cm
LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_Y = 6 # in cm
MIDDLE_SENSOR_DISTANCE_FROM_ROBOT_CENTRE = 6 # in cm
RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_X = 4 # in cm 
RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_Y = 6 # in cm 

DEBUG = False