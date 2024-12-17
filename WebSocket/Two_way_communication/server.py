import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen()
print('Server is running')
socket, address = server.accept()  # 阻塞等待客户端连接

while True:
    data = socket.recv(1024)
    print(data.decode('utf-8'))
    if data.decode() == '再见':
        break

    re_data = input()
    socket.send(re_data.encode())

server.close()
socket.close()

