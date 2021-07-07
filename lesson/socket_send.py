import socket
from config import LOCALHOST

TARGET_PORT = 8889

my_socket = socket.socket()

address_and_port = (LOCALHOST, 27729)

my_socket.connect(address_and_port)

data_amount = my_socket.send(b'"HTTP/1.1 200 OK\n Content-Length: 100\n Connection:'
                b' close\n Content-Type: text/html\n\n <h1>Hello from OTUS!</h1>".encode("utf-8")')

print("send", data_amount, "bytes")

my_socket.close()

