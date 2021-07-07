import socket

HOST = "127.0.0.1"
PORT = 15600

with socket.socket() as s:
    print(f'Connecting to {HOST}:{PORT}')
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(repr(data))
    print(data.decode('utf-8'))
    while True:

        data_to_send = input("Lets send: ")
        data_to_send2 = b'GET / HTTP/1.1\r\nHost: 127.0.0.1:16724\r\nConnection: keep-alive\r\nsec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"\r\nsec-ch-ua-mobile: ?0\r\nDNT: 1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: ru,en-US;q=0.9,en;q=0.8\r\nCookie: _xsrf=2|2e05766e|c4a35f2de2240a5ab7e192cfde24285a|1623234010\r\n\r\n'

        if data_to_send == 'close':
            s.send(bytes(data_to_send.strip(), 'utf-8'))
            print("zakrivau")

        s.send(data_to_send2)
        data = s.recv(1024)
        print("Received back: ", repr(data.decode("utf-8")))
