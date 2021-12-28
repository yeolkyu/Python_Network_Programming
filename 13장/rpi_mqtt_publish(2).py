#라즈베리 파이에 연결된 스위치 상태를 읽어 메시지를 발행하는 프로그램

import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time

SWITCH = 23 #GPIO 23에 스위치 연결
broker = "test.mosquitto.org" #브로커 주소
# broker = "broker.hivemq.com"

def Rpi_Set(): #라즈베리 파이 설정
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SWITCH, GPIO.IN) #GPIO 23 = input mode
    GPIO.setwarnings(False)

topics = ['RPi/SWITCH'] #토픽 지정
print('Topic: ', topics[0])
Rpi_Set()

while True:
    state = GPIO.input(SWITCH) #스위치 상태 읽기
    if state == 1: #스위치 ON
        msg = "ON"
    else: #스위치 OFF
        msg = "OFF"
        
    print("Switch is ", msg)
    publish.single(topics[0], msg, hostname=broker) #메시지 발행
    time.sleep(0.5)