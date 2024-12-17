import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)

socket, address = server.accept()  # 阻塞等待客户端连接

data = socket.recv(1024)
print(data.decode('utf-8'))

socket.send('Hello, {}'.format(data.decode()).encode())
socket.close()
server.close()
