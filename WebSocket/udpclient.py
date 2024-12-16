import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto('Hello, server!'.encode(), ('127.0.0.1', 8888))
print(client.recv(1024).decode())
client.close()