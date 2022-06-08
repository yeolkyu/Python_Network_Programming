# 연습문제 11-6 서버

import socket, pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5000))

print("Waiting for client")

while True:
    # 데이터를 수신하여 원래의 데이터형으로 변환
    data, addr = sock.recvfrom(1024)
    data = pickle.loads(data)
    
    # 수신 데이터를 변환
    num = str(data[0])
    
    # 2진수이면 10진수로 변환
    if data[1] == 'b':
        print("Received number", data[0])
        response = (int(num,2), 'd')
        print("Converted number",response)
        
    # 10진수이면 2진수로 변환
    elif data[1] == 'd':
        print("Received number", data[0])
        response = (format(int(num), 'b'), 'b')
        print("Converted number", response)
    else:
        print("Unknown format")
        
    # 변환 데이터를 바이트로 전송
    sock.sendto(pickle.dumps(response), addr)