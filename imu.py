import time

import FaBo9Axis_MPU9250


class Imu(FaBo9Axis_MPU9250.MPU9250):

    def __init__(self, axis):
        super().__init__()
        self.axis = axis
        self.calibration_parameter = 0
        self.last_measurement_time = None

    def calibrate(self):
        iterations = 1000
        error = 0
        for iteration in range(iterations):
            error += self.measure()
        self.calibration_parameters = error / iterations

        print(self.calibration_parameters)
    def measure(self):
        return self.readGyro()[self.axis] - self.calibration_parameter

    def get_angle_change(self):
        new_measurement_time = time.time()
        yaw_change = - self.measure()
        if not self.last_measurement_time:
            self.last_measurement_time = new_measurement_time
            return None
        dt = new_measurement_time - self.last_measurement_time
        self.last_measurement_time = new_measurement_time
        return yaw_change*dt

    def handle_imu(self):
        angle = 0
        d_angle = self.get_angle_change()
        if d_angle is not None:
            angle += d_angle
            if angle > 360:
                angle -= 360
            if angle < -360:
                angle += 360
        return angle


if __name__ == "__main__":
    try:
        imu = Imu('y')
        imu.calibrate()
        while True:
            angle = imu.handle_imu()
            print(angle)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("User stop")
