import socket
import random

HOST = "127.0.0.1"
PORT = random.randint(10000, 20000)

with socket.socket() as socket:
    socket.bind((HOST, PORT))
    print(f'open adress {HOST} and port {PORT}')
    socket.listen(10)
    connect, addr = socket.accept()

    data = str(connect.recv(1024))


    print("massage----(", data, ")------", connect, addr)

    if "GET" in data:
        print({"Request Method": "GET"})


    data




