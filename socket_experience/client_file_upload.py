import socket

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cli_socket.connect(("192.168.1.78", 10086))

with open("../python.txt", "rb") as src_f:
    while True:
        data = src_f.read(1024)
        if not data:
            break
        cli_socket.send(data)

cli_socket.close()
