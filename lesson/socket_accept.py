import socket
from config import LOCALHOST

my_socket = socket.socket()

address_and_port = (LOCALHOST, 8889)

my_socket.bind(address_and_port)

print("start socket on", address_and_port)

my_socket.listen(10)

conn, addr = my_socket.accept()

print(conn, addr)

my_socket.close()
