#타임 클라이언트 프로그램

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))
print(sock.recv(1024).decode())

sock.close()
