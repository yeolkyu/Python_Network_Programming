#프레임 생성과 파싱 프로그램

import socket
import capsule

SIZE = 5 #분할 크기
sock = socket.socket()
sock.connect(('localhost', 2500))

HEAD = 0x05 #시작문자
addr = 1 #상대방 주소
seqNo=1 #순서번호
frame_seq=""
msg = "hello world"
print("전송 메시지: ", msg)
for i in range(0, len(msg), SIZE): #5문자씩 분할하여 프레임 구성
    start = i
    frame_seq += capsule.frame(HEAD, addr, seqNo, msg[start:start+SIZE])
    start += SIZE
    seqNo += 1

sock.send(frame_seq.encode()) #프레임 전송
msg = sock.recv(2048).decode() #프레임 다시 수신
print("수신 프레임: ",msg)
r_frame = msg.split(chr(0x05)) #프레임 분할
del r_frame[0]

p_msg=''
for fr in r_frame:
    p_msg += fr[10:(11+int(fr[6:10]))] #메시지 복원
print("복원 메시지: ",p_msg)
sock.close()