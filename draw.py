from math import cos, sin

from matplotlib import pyplot as plt


def calculate_x_from_distance_and_angle(distance: float, angle: float) -> float:
    return cos(angle) * distance


def calculate_y_from_distance_and_angle(distance: float, angle: float) -> float:
    return 


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
