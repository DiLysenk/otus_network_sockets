import socket
from config import LOCALHOST, random_port




default_socket = socket.socket() #сокет создается по умолчанию

address_and_port = (LOCALHOST, 3000)

default_socket.bind(address_and_port)

print("socket 1 bindet on", address_and_port)

default_socket.close()


