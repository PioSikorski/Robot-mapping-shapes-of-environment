import socket
import threading
import time

from control import Move
from imu import Imu
from enkoder import Encoder
from control import Move
from consts import PI_IP_ADDRESS, SERVER_PORT, LEFT_ENCODER_SENSOR_PIN, RIGHT_ENCODER_SENSOR_PIN

# https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


class Server:
    def __init__(self):
        s = socket.socket()
        binded = False
        while not binded:
            try:
                s.bind((PI_IP_ADDRESS, SERVER_PORT))
                binded = True
            except socket.error:
                pass
            except KeyboardInterrupt:
                exit()
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.listen(1)
        self.conn, self.addr = s.accept()
        self.t = StoppableThread(target=self._serve)

        self.m = Move((25, 8, 7), (14, 15, 18))
        self.steer_cmds = {
            'f': self.m.movF,
            'b': self.m.movB,
            'r': self.m.movR,
            'l': self.m.movL,
            's': self.m.stop
        }

    def serve(self):
        self.m.initialize_motors()
        self.t.start()
        print(f"Socket Up and running with a connection from {self.addr}")

    def _serve(self):
        while True:
            rcvdData = self.conn.recv(1024).decode()

            if rcvdData:
                steer_cmd = rcvdData[-1]
                print(f"Received data: {rcvdData} | Steer signal: {steer_cmd}")
                self.steer_cmds.get(steer_cmd, Move.stop)()

    def stop_serving(self):
        print(1)
        self.t.stop()
        print(2)
        self.t.join()
        print(3)
        self.conn.close()
        print(4)


if __name__ == "__main__":
    server = Server()
    try:
        server.serve()
    except KeyboardInterrupt:
        server.stop_serving()
