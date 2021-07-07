import socket
HOST = "127.0.0.1"

with socket.socket() as socket:
    socket.connect((HOST, 11110))
    data_amount = socket.send("HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close"
                     "\n Content-Type: text/html\n\n <h1>Hello from OTUS!</h1>".encode("utf-8"))
    print("send", data_amount, "bytes")
