#UDP 소켓을 이용한 파일 송수신 프로그램
#수신을 먼저 실행하고 송신한다

import socket, time, sys

BUFSIZE = 1024*8

def Receiver():
    sock.bind(addr)
    
    print("수신 대기 중...")
    file_name, client = sock.recvfrom(BUFSIZE) #파일 이름 수신
    sock.sendto('ok'.encode(), client) #응답
    
    with open('d:/'+file_name.decode(), "wb") as fp:
        print("파일 수신 중...")
        while True:
            data = sock.recvfrom(BUFSIZE)
            if not data[0]: #수신 완료
                break
            fp.write(data[0]) #수신 데이터를 파일에 저장
    
    print("수신 완료")

def Sender():
    file_name = input("File name to send: ")
    sock.sendto(file_name.encode(), addr) #파일 이름 전송
    resp, client = sock.recvfrom(BUFSIZE) #응답 수신
    
    if resp.decode().lower() == 'ok':
        fp = open(file_name, "rb")
        data = fp.read(BUFSIZE)
        print("송신 중...")
    
        while(data):
            sock.sendto(data, client)
            time.sleep(0.02) #수신측에서 저장할 때까지 잠시 대기
            data = fp.read(BUFSIZE)
            
        sock.sendto(data, client) #송신 완료를 위해 빈 데이터 전송
        fp.close()
        print("전송 완료")
    else:
        print("수신 응답 오류")

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('localhost', 2500)
    try:
        role = sys.argv[1] #송신(s) 또는 수신(r)
        if role == 's':
            Sender()
        elif role == 'r':
            Receiver()
        else:
            print("s(송신) 또는 r(수신)을 지정하세요")
    except:
        print("s(송신) 또는 r(수신)을 지정하세요")