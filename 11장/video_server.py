# Video server
# Capturing a video stream from webcam and sending it to client

import socket, cv2, pickle, struct, imutils

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_PORT = 9000
server_addr = ('', TCP_PORT)

# 주소와 포트번호 바인드
server_socket.bind(server_addr)

# 접속 대기
server_socket.listen(5)
print("서버 접속 대기:", server_addr)

# 클라이언트 연결
while True:
    client_socket, addr = server_socket.accept()
    print(addr, '와 연결됨')
    if client_socket:
        # WebCAM 사용
        vid = cv2.VideoCapture(0) # WebCam
        if vid.isOpened():
            print('width: {}, height: {}'.format(vid.get(3), vid.get(4)))
        #vid.set(3, 320)  # defualt = 640 x 480
        #vid.set(4, 240)

        # 동영상 플레이
        #vid = cv2.VideoCapture("동양미래대학교.mp4") # WebCam
        #if vid.isOpened(): print('width: {}, height : {}'.format(vid.get(3), vid.get(4)))

        while (vid.isOpened()):
            img, frame = vid.read() # 프레임 획득
            #frame = imutils.resize(frame, width=640) # 프레임 크기 조절
            frame_bytes = pickle.dumps(frame) # 프레임을 바이트 스트림으로 변환
            message = struct.pack("Q", len(frame_bytes)) + frame_bytes # frame 길이(unsigned 8bytes) + frame
            client_socket.sendall(message) # 길이 + 프레임 전송

            cv2.imshow('Server Video', frame) # 전송 영상 표시
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
