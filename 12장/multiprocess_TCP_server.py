# multiprocessing 모듈을 이용한 TCP 서버 프로그램

from socket import socket
from multiprocessing import Process

def handle(sock): #자식 프로세스로 실행할 함수
    #문자를 수신하여 표시하고 다시 전송
    while True:
        msg = sock.recv(1024)
        print(f'Received message: {msg.decode()}')
        sock.send(msg)
    
if __name__ == "__main__":
    sock = socket()
    addr = ('', 2500)
    sock.bind(addr)
    sock.listen(4)
    
    while True:
        c_sock, r_addr = sock.accept()
        print(f'{r_addr} is connected')
        p1 = Process(target=handle, args=(c_sock,)) #자식프로세스 생성
        p1.start() #자식 프로세스 시작