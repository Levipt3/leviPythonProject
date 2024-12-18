import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
print('client is running')

# 输入用户名
username = input("请先输入用户名：")
client.send(username.encode())

# 使用锁来控制对 socket 连接的访问
lock = threading.Lock()

def receive(client):
    """ 接收来自服务器的数据并处理 """
    while True:
        try:
            data = client.recv(1024)
            if not data:  # 如果没有数据，可能连接已关闭
                print('Server has closed the connection.')
                break

            message = data.decode()
            print(message)
            if message == '再见':
                print('Server is closing')
                break
        except UnicodeDecodeError:
            print('接收到无法解码的数据.')
            break
        except Exception as e:
            print(f'Error while receiving data: {e}')
            break
    client.close()


def send(client):
    """ 发送用户输入到服务器 """
    while True:
        try:
            message = input()
            if message:  # 确保发送的消息不为空
                with lock:
                    client.send(message.encode('utf-8'))
                if message == '再见':
                    print('Client is closing')
                    client.close()
                    break
        except Exception as e:
            print(f'Error while sending data: {e}')
            break


# 创建和启动接收和发送线程
receive_thread = threading.Thread(target=receive, args=(client,))
send_thread = threading.Thread(target=send, args=(client,))
receive_thread.start()
send_thread.start()

