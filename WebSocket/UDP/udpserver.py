import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8888))
data, addr = server.recvfrom(1024)
print(data.decode())
server.sendto(b'Hello, client!', addr)
server.close()