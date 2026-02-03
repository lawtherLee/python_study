import socket
import threading


def handle_client(client_socket, addr):
    print(f"客户端已连接...{addr}")
    try:
        while True:
            # 接收数据
            recv_data = client_socket.recv(1024)
            if not recv_data:
                break
            message = recv_data.decode("utf-8")
            print(f"接受到的数据：{message},发送自 {addr}")
    finally:
        client_socket.close()
        print(f"客户端已断开连接...{addr}")


def main():
    server = None
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 8080))
        server.listen(5)
        print("服务器已启动，等待客户端连接...")
        while True:
            client_socket, addr = server.accept()
            # 创建线程处理客户端请求
            client_thread = threading.Thread(
                target=handle_client, args=(client_socket, addr)
            )
            # 启用守护线程
            client_thread.daemon = True
            # 挂起线程
            client_thread.start()

    finally:
        if server:
            server.close()


if __name__ == "__main__":
    main()
