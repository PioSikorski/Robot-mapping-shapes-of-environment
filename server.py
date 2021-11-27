import socket
import threading
import time

import control
from imu import Imu
from enkoder import Encoder
from control import Move
from consts import PI_IP_ADDRESS, SERVER_PORT, LEFT_ENCODER_SENSOR_PIN, RIGHT_ENCODER_SENSOR_PIN

steer_cmds = {
    'f': Move.movF,
    'b': Move.movB,
    'r': Move.movR,
    'l': Move.movL,
    's': Move.stop
}


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
        self.t = threading.Thread(target=self._serve)
        
        self.m = Move((14, 15, 18), (25, 8, 7))
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
        self.t.join()
        self.conn.close()


if __name__ == "__main__":
    server = Server()
    try:
        server.serve()
    except KeyboardInterrupt:
        server.stop_serving()
