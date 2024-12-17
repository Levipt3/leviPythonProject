import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
client.send('LiuMingYang'.encode())

data = client.recv(1024)
print(data.decode())

client.close()