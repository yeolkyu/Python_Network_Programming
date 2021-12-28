import socket
help(socket.gethostbyname)

addrinfo = socket.getaddrinfo('www.naver.com',80)

for i in range(len(addrinfo)):
    print(addrinfo[i])