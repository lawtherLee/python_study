import socket

# 创建服务端套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址端口号
server_socket.bind(("192.168.1.78", 12306))

# 允许最大监听数
server_socket.listen(5)
print("等待客户端连接...")
accept_socket, client_address = server_socket.accept()
print("客户端已连接...")
# 发送数据
send_data = "hello client"
accept_socket.send(send_data.encode("utf-8"))
while True:
    # 接收数据
    recv_data = accept_socket.recv(1024)
    print(f"接受到的数据：{recv_data.decode("utf-8")},发送自 {client_address}")

    if recv_data.decode("utf-8") == "exit":
        break
accept_socket.close()
# 设置端口号重用 用于立即释放端口占用
# 参1 代表当前socket对象
# 参2 端口号重用
# 参3 重用值
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
