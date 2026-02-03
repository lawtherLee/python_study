import socket


def send_message(client_socket, message):
    try:
        client_socket.sendall(message.encode("utf-8"))
        print(f"已发送数据：{message}")
    except Exception as e:
        print(e)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(("localhost", 8080))
        while True:
            message = input("请输入要发送的数据(输入exit退出）:")
            if message == "exit":
                break
            send_message(client, message)
    finally:
        client.close()
        print("已关闭连接")


if __name__ == "__main__":
    main()
