import socket

# 创建服务端套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址端口号
server_socket.bind(("192.168.1.78", 10086))

# 允许最大监听数
server_socket.listen(5)

count = 0
while True:
    count += 1
    print("等待客户端连接...")
    accept_socket, client_address = server_socket.accept()
    print("客户端已连接...")

    # file_name = "./data/图片_" + str(count) + ".png"
    with open("python.txt", "wb") as dest_f:
        while True:
            data = accept_socket.recv(1024)
            if not data:
                break
            dest_f.write(data)
    accept_socket.close()
