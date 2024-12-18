import socket
import threading

# 创建一个 TCP 套接字并设置服务器监听
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
print('Server is running')

client_sockets = {}  # 存储所有客户端连接对象
lock = threading.Lock()  # 线程锁，确保线程安全


# 处理每个客户端连接的函数
def handle_socket(sock):
    try:
        username = sock.recv(1024).decode()  # 接收用户名

        # 添加用户到字典
        with lock:
            client_sockets[sock] = username
            welcome_message = f"欢迎[{username}] 加入群聊！".encode()
            for client in client_sockets.keys():
                client.send(welcome_message)

        while True:
            data = sock.recv(1024).decode()
            if not data:  # 客户端关闭连接
                break

            send_data = (username + "说：" + data).encode()
            if data.startswith('@'):  # 处理指令
                msg = data.split(' ')  # 修正为split方法
                private_name = msg[0][1:]

                with lock:
                    for k, v in client_sockets.items():
                        if v == private_name:
                            k.send(send_data)  # 不需要再次encode
            else:  # 处理普通消息
                with lock:
                    for client in client_sockets:
                        if client != sock:  # 发送消息给其他客户端除了自己
                            client.send(send_data)  # 将接收到的数据发送给所有客户端
                print("消息转发成功！")
    except Exception as e:
        print(f"错误: {e}")
    finally:
        with lock:  # 确保线程安全地移除用户
            if sock in client_sockets:
                username = client_sockets[sock]  # 取出用户名以便发送离开通知
                client_sockets.pop(sock)
                for client in client_sockets:
                    client.send((username + " 离开了群聊！").encode())
                sock.close()  # 关闭连接


# 服务器主循环，接受客户端连接
while True:
    sock, addr = server.accept()  # 阻塞方式，接受不同的客户端连接请求
    print(f"客户端连接成功: {addr}")
    client_thread = threading.Thread(target=handle_socket, args=(sock,))
    client_thread.start()
