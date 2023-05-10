# 동영상 수신
import socket
import numpy
import cv2

def close_all(out, sock):
    out.release()
    sock.close()
    cv2.destroyAllWindows()
    
UDP_IP = ""
UDP_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(10) # client와 연결이 종료되었는지 확인하기 위해 timeout 필요
sock.bind((UDP_IP, UDP_PORT))

# 640 x 480 칼라 프레임 저장 버퍼
buffer = [b'\xff' * 46080 for x in range(20)] # 640 x 480 x 3 = 46080 x 20

# 동영상 파일의 fourcc 값 가져오기(코덱, 압축 방식, 색상, 픽셀 포멧 등)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # DIVX MPEG-4 코덱('D','I','V','X')

# 동영상을 파일에 저장
# VideoWriter(filename, fourcc, fps, frameSize, isColor=None) 객체 생성
out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (640,480))
print("Waiting for video...")

while True:
    picture = b''

    # 프레임을 수신하여 버퍼에 저장
    try:
        data, addr = sock.recvfrom(46081) # 데이터가 수신되지 않으면 timeout 예외 발생
    except:
        close_all(out,sock)
        break
    
    buffer[data[0]] = data[1:46081] # frame(46081) = frame_number(0) + frame_data(46080)

    if data[0] == 19: # 마지막 프레임?
        for i in range(20):
            picture += buffer[i] # 프레임 직렬화

        # 이진 문자열을 정수 배열로 변환
        frame = numpy.frombuffer(picture, dtype=numpy.uint8)
        
        # 640 x 480 x 3으로 변환
        frame = frame.reshape(480, 640, 3)
        
        # 프레임 표시
        cv2.imshow("Server Frame", frame)
        
        # frame을 동영상 파일에 저장
        out.write(frame) 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_all(out,sock)
            break