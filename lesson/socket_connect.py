import socket
from config import LOCALHOST

my_socket = socket.socket()

TARGET_PORT = None

address_and_port = (LOCALHOST, TARGET_PORT)

my_socket.connect(address_and_port)
my_socket.close()