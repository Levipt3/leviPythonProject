import socket,threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
print('Server is running')


def handle_socket(socket):
    while True:
        data = socket.recv(1024)
        print(data.decode('utf-8'))
        re_data = input()
        socket.send(re_data.encode())


while True:
    socket, address = server.accept()  # 阻塞等待客户端连接
    client_thread = threading.Thread(target=handle_socket, args=(socket,))
    client_thread.start()

