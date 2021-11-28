import csv
from math import cos, pi, sin

from matplotlib import pyplot as plt

LEFT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE = -30  # degrees
MIDDLE_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE = 0  # degrees
RIGHT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE = 30  # degrees


def get_x_part(distance: float, angle: float) -> float:
    """
    @param distance: distance in meters
    @param angle: angle in degrees
    """
    angle_in_radians = 2*pi * angle / 360
    return cos(angle_in_radians) * distance


def get_y_part(distance: float, angle: float) -> float:
    """
    @param distance: distance in meters
    @param angle: angle in degrees
    """
    angle_in_radians = 2*pi * angle / 360
    return sin(angle_in_radians) * distance


def draw(input_data: list):
    """
    @param input_data: list in format [[robot_x, robot_y, robot_angle, left, middle, right], ...]
    """
    robot_xs, robot_ys = [], []
    left_xs, left_ys = [], []
    middle_xs, middle_ys = [], []
    right_xs, right_ys = [], []
    input_data = input_data[1:]
    for measure in input_data:
        print(measure)
        for robot_x, robot_y, robot_angle, left, middle, right in measure:
            robot_xs.append(robot_x)
            robot_ys.append(robot_y)

            left_xs.append(robot_x +
                           get_x_part(left, robot_angle + LEFT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))
            left_ys.append(robot_y +
                           get_y_part(left, robot_angle + LEFT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))

            middle_xs.append(robot_x +
                             get_x_part(left, robot_angle + MIDDLE_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))
            middle_ys.append(robot_y +
                             get_y_part(left, robot_angle + MIDDLE_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))

            right_xs.append(robot_x +
                            get_x_part(left, robot_angle + RIGHT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))
            right_ys.append(robot_y +
                            get_y_part(left, robot_angle + RIGHT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))

    plt.plot(robot_xs, robot_ys)
    plt.plot(left_xs, left_ys)
    plt.plot(middle_xs, middle_ys)
    plt.plot(right_xs, right_ys)
    plt.show()


def read_data(file_path: str) -> list:
    data = []
    with open(file_path, 'r') as f:
        r = csv.reader(f)
        for line in r:
            # process each line
            data.append(line)
    return data

if __name__ == "__main__":
    input_data = read_data('res.csv')
    draw(input_data)
