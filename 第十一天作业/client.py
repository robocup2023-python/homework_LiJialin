import socket
client = socket.socket()
client.connect(('127.0.0.1',8680))
client.sendall((input()).encode('utf-8'))
print(client.recv(1024).decode())