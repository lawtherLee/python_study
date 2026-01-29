import socket

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cli_socket.connect(("192.168.1.78", 12306))

recv_data = cli_socket.recv(1024)
print("接收到的数据为：%s" % recv_data.decode("utf-8"))

while True:
    send_data = input("请输入要发送的数据：")
    if not send_data:
        break
    cli_socket.send(send_data.encode("utf-8"))
    if send_data == "exit":
        break
cli_socket.close()
