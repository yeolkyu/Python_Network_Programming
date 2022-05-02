# 간단한 TCP 클라이언트 프로그램

import socket

port = 2500
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
while True:
    msg = input("Message to send: ")
    if not msg: break
    s.send(msg.encode()) #send a message to server
    r_msg = s.recv(BUFSIZE) #receive message from server
    
    print("Received message: %s" %r_msg.decode())

s.close()