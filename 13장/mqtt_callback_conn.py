# 플래그를 이용하여 브로커와의 연결을 세부적으로 확인하는 프로그램

import paho.mqtt.client as mqtt
import time
import sys

def on_connect(client, userdata, flags, rc):
    if rc == 0: #연결 성공
        client.connected_flag = True
        print("connected OK")
    else: #연결 실패
        print('Bad connection Returen code= ', rc)
        client.bad_connected_flag = True

mqtt.Client.connected_flag = False #연결 성공 플래그 인스턴수 변수 추가
mqtt.Client.bad_connected_flag = False #연결 실패 플래그 인스턴수 변수 추가

broker = 'test.mosquitto.org' #브로커 주소
client = mqtt.Client() #클라이언트 객체 생성
client.on_connect = on_connect #연결 콜백 함수 지정
print('Connecting to broker ', broker)

try:
    client.connect(broker) #브로커와 연결
except:
    print("연결 실패")
    sys.exit(1)
          
client.loop_start() #이벤트 루프 시작

#연결 성공 여부를 세부적으로 확인한다
while not client.connected_flag and not client.bad_connected_flag: 
    print('In wait loop')
    time.sleep(1)

    #연결이 실패면 이벤트 루프 종료
    if client.bad_connected_flag == True:
        client.loop_stop()
        sys.exit(1)
    
print('in Main Loop')
client.publish('mqtt/test', 'Hello World') #메시지 발행
time.sleep(4)
client.loop_stop() #이벤트 루프 종료
client.disconnect() #연결 해제