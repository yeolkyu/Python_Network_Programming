from socket import *

sock = socket(AF_INET, SOCK_STREAM)
addr = ("", 2500)
sock.bind(addr)
sock.listen(5)
print("접속 대기 중")
count = 1

while True:
    c_sock, c_addr = sock.accept()
    print(f"{count}번째 클라이언트가 접속하였습니다")
    c_sock.send(f"당신은 {count}번째 접속자입니다".encode())
    count += 1
    c_sock.close()