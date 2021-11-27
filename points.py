from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


def get_midpoint(p1: Point, p2: Point) -> Point:
    """
    return Point between two given points
    """
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)