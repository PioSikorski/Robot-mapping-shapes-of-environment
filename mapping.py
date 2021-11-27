from dataclasses import dataclass
from matplotlib import pyplot as plt
import time
from math import pi, sin, cos

l = [60.94473600387573, 62.18366622924805, 61.357712745666504, 62.17139959335327, 61.382246017456055, 62.17548847198486, 62.26135492324829, 62.22864389419556, 61.42313480377197, 61.77886724472046,
     61.84428930282593, 61.34135723114014, 61.29637956619263, 61.37815713882446, 61.37406826019287, 63.17317485809326, 61.361801624298096, 60.907936096191406, 61.77477836608887, 59.35416221618652, 60.973358154296875]
m = [95.99460363388062, 74.21314716339111, 53.24128866195679, 44.69553232192993, 75.90185403823853, 75.93047618865967, 75.91003179550171, 75.5134105682373, 92.86661148071289, 75.566565990448,
     81.68761730194092, 75.03092288970947, 75.5134105682373, 75.50932168960571, 82.97970294952393, 49.11152124404907, 74.23768043518066, 48.2487678527832, 75.5134105682373, 81.73259496688843, 74.14772510528564]
r = [210.16427278518677, 23.75638484954834, 44.60557699203491, 73.39128255844116, 162.52474784851074, 50.71436166763306, 144.67270374298096, 64.97228145599365, 84.86876487731934, 33.31209421157837,
     54.86457347869873, 98.51335287094116, 69.90755796432495, 112.84487247467041, 98.15762042999268, 56.59825801849365, 309.9451780319214, 59.75487232208252, 64.52250480651855, 33.52471590042114, 70.3328013420105]

xl = []
yl = []
xr = []
yr = []


@dataclass
class Point:
    x: float
    y: float


def get_midpoint(p1: Point, p2: Point) -> Point:
    """
    return Point between two given points
    """
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)

# points = []
# while True:
    # update imu
    # update enkoder
    # pobierz dane z czujnikow odleglosciowych
    # points.append(
        # {obecna pozycja robota:Point: {
        #     left: lewy czujnik
        #     middle: srodkowy
        #     right: prawy           
        # }}
        # )

points = []
# opcja 1 # polozenie robota + pomiar z czujnikow niegotowe
points.append(
    {
        Point(1, 2):
        {
            "left_sensor": Point(3, 4),
            "middle_sensor": Point(4, 4),
            "right_sensor": Point(5, 5)
        }
    }
)
robot = []
left = []
middle = []
right = []
for pomiar in points:
    for pozycja_robota, czujniki in pomiar.items():


# opcja 2 # polozenie robota + gotowe pomiary z czujnikow
points.append(
    {
        Point(1, 2):
        {
            #"left_sensor": policz_z czujnika...Point(3, 4), 
            "middle_sensor": Point(4, 4),
            "right_sensor": Point(5, 5)
        }
    }
)


class Map:

    def __init__(self, left, middle, right):
        self.left = left
        self.middle = middle
        self.right = right

    def draw(self):
        robot_position = xl
        plt.plot(robot_position, yl)
        plt.plot(self.left, self.right)
        plt.legend(['lewe', 'prawe'])
        plt.show()

    def read_data(self):
        with open('RIGHT_result_file.txt', 'r') as f1:
            for line in f1:
                r.append(line.strip('\n'))

        with open('MIDDLE_result_file.txt', 'r') as f2:
            for line in f2:
                m.append(line.strip('\n'))

        with open('LEFT_result_file.txt', 'r') as f3:
            for line in f3:
                l.append(line.strip('\n'))

        with open('encoder_path_left_wheel.txt', 'r') as f4:
            for line in f4:
                p = line.split(',')
                xl.append(float(p[0]))
                yl.append(float(p[1]))

        with open('encoder_path_right_wheel.txt', 'r') as f5:
            for line in f5:
                p = line.split(',')
                xr.append(float(p[0]))
                yr.append(float(p[1]))

        for x in range(len(xl)):
            xl[x] = xl[x] * 100
        for y in range(len(yl)):
            yl[y] = yl[y] * 100

        for x in range(len(xr)):
            xr[x] = xr[x] * 100
        for y in range(len(yr)):
            yr[y] = yr[y] * 100

    def sensors_data(self, sensor):
        for i in range(len(sensor)):
            x = float(sensor[i]) * sin(30 * pi / 100)
            y = float(sensor[i]) * cos(30 * pi / 100)


map = Map(l, m, r)
map.read_data()
map.sensors_data(r)
map.sensors_data(m)
map.sensors_data(l)
print(r)
map.draw()
