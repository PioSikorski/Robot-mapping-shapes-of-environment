from math import cos, pi, sin

from matplotlib import pyplot as plt


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


def draw(input_data -> list):
    """
    @param input_data: list in format [[robot_x, robot_y, left, middle, right], ...]
    """
    robot_xs, robot_ys = [], []
    left_xs, right_ys = [], []
    middle_xs, middle_ys = [], []
    right_xs, right_ys = [], []

    for measure in input_data:
        for robot_x, robot_y, left, middle, right in measure:
            robot_xs.append(robot_x)
            robot_ys.append(robot_y)
            left_xs.append(robot_x)