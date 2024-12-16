import socket

# 创建一个tcp链接
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口
server.bind(('0.0.0.0', 8000))

# 监听链接
server.listen(5)

# sock本次链接所创建的socket对象，addr是客户端的地址
sock, addr = server.accept()  # 阻塞方法

data = sock.recv(1024)  # 接收数据

print(data.decode())  # 打印接收到的数据

sock.send("Hello, client!".encode())  # 发送数据

sock.close()  # 关闭链接
