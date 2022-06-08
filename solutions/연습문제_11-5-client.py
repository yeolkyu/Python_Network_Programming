# 연습문제 11-6 클라이언트

import socket, pickle

BUFFSIZE = 1024
port = 5000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP 소켓

# 변환할 데이터
msg = (11001, 'b')
#msg = (123, 'd')
print("Original number", msg)

# 데이터를 바이트로 변환하여 전송
sock.sendto(pickle.dumps(msg),('localhost', port)) #메시지 전송

# 응답을 수신하여 원래의 데이터형으로 출력
data, addr = sock.recvfrom(BUFFSIZE) #데이터 수신
print("Converted number", pickle.loads(data))
