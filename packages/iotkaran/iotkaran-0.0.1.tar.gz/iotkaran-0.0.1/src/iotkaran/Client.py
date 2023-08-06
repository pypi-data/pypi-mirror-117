import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




    def connect(self):
        print("connect to server iotkaran " + self.host  )
        self.socket.connect((self.host, self.port))


    def diconnect(self):
        print("connect to server iotkaran " + self.host + self.port)
        self.socket.close()

    def send(self,messeg):
        self.socket.sendall(messeg)

    def status(self):

        print("connect " +self.socket)


iotk = Client("server.iotkaran.ir", 2323)
iotk.connect()
iotk.status()
iotk.send(b'asdasdasd\r\n')