import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self):
        print("connect to server iotkaran " )
        self.socket.connect((self.host, self.port))

    def diconnect(self):
        print("disconnect As iotkaran ")
        self.socket.close()

    def send(self,messeg):
        self.socket.sendall(messeg)

