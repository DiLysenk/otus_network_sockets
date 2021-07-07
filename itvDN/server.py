import socket
import random

HOST = "127.0.0.1"
PORT = random.randint(10000, 20000)
addres_port = (HOST, PORT)
with socket.socket() as s:
    s.bind(addres_port)  # биндим порт

    print(f'open adress and port -- curl {HOST}:{PORT}')  # сообщение о адресе и порте

    s.listen()  # слушаем порт и адрес
    connect, address = s.accept()  # создание сокета для подключения

    data = connect.recv(4096)

    request_method = data.decode('utf-8').split()[0]
    headers = data.decode('utf-8').split('\r\n')[8:]


    response_status = 200

    massage = f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: text/html\n\n <h1>Request Method: {request_method} " \
              f"Request Source: {addres_port} Response Status: {response_status} OK {headers}</h1>".encode("utf-8")

    connect.send(massage)




