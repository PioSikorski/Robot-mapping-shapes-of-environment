from motor import Motor


class Move():
    def __init__(self, left_wheel_params, right_wheel_params):
        self.left_wheel_params = left_wheel_params
        self.right_wheel_params = right_wheel_params
        self.motor_left = None
        self.motor_right = None

    def initialize_motors(self):
        self.motor_left = Motor(*self.left_wheel_params)
        self.motor_right = Motor(*self.right_wheel_params)

    def movF(self):
        self.motor_right.moveF()
        self.motor_left.moveF()

    def movB(self):
        self.motor_right.moveB()
        self.motor_left.moveB()

    def movL(self):
        self.motor_left.moveF()
        self.motor_right.stop()

    def movR(self):
        self.motor_right.moveF()
        self.motor_left.stop()

    def stop(self):
        self.motor_right.stop()
        self.motor_left.stop()
