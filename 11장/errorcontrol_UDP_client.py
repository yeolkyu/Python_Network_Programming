# 오류제어 기능이 포함된 UDP 클라이언트 프로그램

import random
from socket import *

port = 2500
BUFFER = 1024
server = "localhost"
c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect((server, port))

for i in range(10): #10번 시도
    delay = 0.1  #0.1초부터 지연 시작
    data = 'Hello message'

    while True:
        c_sock.send(data.encode())
        print(f'Waiting up to {delay} seconds for a reply')
        c_sock.settimeout(delay) #타임아웃 설정
        try:
            data = c_sock.recv(BUFFER) #데이터 수신
        except timeout: #타임아웃 발생
            delay *= 2  #대기 시간 2배 증가
            if delay > 2.0: #시간 초과
                print('The server seems to be down')
                break 
        else:
            print('Response: ', data.decode())
            break #종료
