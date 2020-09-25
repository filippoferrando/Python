import socket

s = socket.socket()
host = socket.hostname()
port = 4444
s.bind((host, port))

s.listen(5)

while True:
    c.addr = s.accept()
    print("connection from ", addr)
    c.send("Success connected")
    c.close()