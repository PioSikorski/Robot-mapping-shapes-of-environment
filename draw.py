import csv
from math import cos, pi, sin

from matplotlib import pyplot as plt
from consts import LEFT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE, LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_X, LEFT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_Y, MIDDLE_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE, MIDDLE_SENSOR_DISTANCE_FROM_ROBOT_CENTRE, RIGHT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE, RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_X, RIGHT_SENSOR_DISTANCE_FROM_ROBOT_CENTRE_Y

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
    f_left_xs, f_left_ys = [], []
    middle_xs, middle_ys = [], []
    f_middle_xs, f_middle_ys = [], []
    right_xs, right_ys = [], []
    f_right_xs, f_right_ys = [], []
    input_data = input_data[1:]
    i = 0
    for measure in input_data:
        # i += 1
        # if i > 88:
        #     break
        robot_x, robot_y, robot_angle, left, middle, right = [float(x) for x in measure]
        
        #for robot_x, robot_y, robot_angle, left, middle, right in measure:
        robot_x *= 100
        robot_y *= 100
        robot_xs.append(robot_x)
        robot_ys.append(robot_y)

        if left < 200:
            left_xs.append(robot_x +
                            get_x_part(left, robot_angle + LEFT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))
            left_ys.append(robot_y +
                            get_y_part(left, robot_angle + LEFT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))

        if middle < 200:
            middle_xs.append(robot_x +
                                get_x_part(middle, robot_angle + MIDDLE_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))
            middle_ys.append(robot_y +
                                get_y_part(middle, robot_angle + MIDDLE_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))
        if right < 200:
            right_xs.append(robot_x +
                            get_x_part(right, robot_angle + RIGHT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))
            right_ys.append(robot_y +
                            get_y_part(right, robot_angle + RIGHT_DISTANCE_SENSOR_ANGLE_FROM_ROBOT_CENTRE))

    for i in range(5, len(left_xs)):
        f_left_xs.append((left_xs[i-4]+left_xs[i-3]+left_xs[i-2]+left_xs[i-1]+left_xs[i])/5)
        f_left_ys.append((left_ys[i-4]+left_ys[i-3]+left_ys[i-2]+left_ys[i-1]+left_ys[i])/5)
    for i in range(5, len(middle_xs)):
        f_middle_xs.append((middle_xs[i-4]+middle_xs[i-3]+middle_xs[i-2]+middle_xs[i-1]+middle_xs[i])/5)
        f_middle_ys.append((middle_ys[i-4]+middle_ys[i-3]+middle_ys[i-2]+middle_ys[i-1]+middle_ys[i])/5)
    for i in range(5, len(right_xs)):
        f_right_xs.append((right_xs[i-4]+right_xs[i-3]+right_xs[i-2]+right_xs[i-1]+right_xs[i])/5)
        f_right_ys.append((right_ys[i-4]+right_ys[i-3]+right_ys[i-2]+right_ys[i-1]+right_ys[i])/5)
    plt.plot(robot_xs, robot_ys, 'r.')
    #plt.plot(left_xs, left_ys, 'blue', linewidth=0.1, marker='.')
    plt.plot(f_left_xs, f_left_ys, 'green', linewidth=0.1, marker='.')
    plt.plot(middle_xs, middle_ys, 'cyan', linewidth=0.1, marker='.')
    plt.plot(right_xs, right_ys, 'purple', linewidth=0.1, marker='.')
    plt.legend(["Robot", "SENSOR L", "SENSOR M", "SENSOR R"])
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
