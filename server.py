import socket
import random
from http import HTTPStatus

HOST = "127.0.0.1"
PORT = random.randint(10000, 20000)
addres_port = (HOST, PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(addres_port)  # биндим порт

    print(f'open adress and port -- curl {HOST}:{PORT}')  # сообщение о адресе и порте

    s.listen()  # слушаем порт и адрес
    connect, address = s.accept()  # создание сокета для подключения

    data = connect.recv(4096)

    request_method = data.decode('utf-8').split()[0]
    headers = data.decode('utf-8').split('\r\n')[8:]
    headers_pretty = ''
    for i in headers:
        headers_pretty = headers_pretty + i + '\n'

    if b"status=404" in data:
        status_valuse = HTTPStatus.NOT_FOUND.value
        status_phrase = HTTPStatus.NOT_FOUND.phrase
    elif b"status=200" in data:
        status_valuse = HTTPStatus.OK.value
        status_phrase = HTTPStatus.OK.phrase
    else:
        status_valuse = HTTPStatus.OK.value
        status_phrase = HTTPStatus.OK.phrase

    massage = f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: text/html\n\n <h1>Request Method: {request_method} " \
              f"Request Source: {addres_port} Response Status: {status_valuse} {status_phrase} {headers_pretty}</h1>".encode(
        "utf-8")

    connect.send(massage)
