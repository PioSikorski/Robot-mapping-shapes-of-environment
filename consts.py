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
PI_IP_ADDRESS = "192.168.0.201" # raspberry pi IP address
HOST_IP_ADDRESS = "192.168.0.25" # host IP address
SERVER_PORT = 5050