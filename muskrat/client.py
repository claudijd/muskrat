import paramiko
import socket
from muskrat import Banner


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.user = 'root'
        self.password = ''
        self.banner = Banner("")

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        raw_banner = sock.recv(1024)
        self.banner = Banner(raw_banner)

        # TODO: Make the client dance more!
