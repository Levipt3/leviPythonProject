import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
print('client is running')
while True:
    to_data = input()
    client.send(to_data.encode())  # 发送数据
    data = client.recv(1024)
    print(data.decode())
    if data.decode() == '再见':
        print('Server is closing')
        break
client.close()
