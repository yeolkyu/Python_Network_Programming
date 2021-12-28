# mqtt_subscribe_simple.py
# MQTT 메시지 구독 프로그램

import paho.mqtt.subscribe as subscribe

topics = 'mqtt/multiple'

messages = 2
m = subscribe.simple(topics, hostname="test.mosquitto.org",
                     retained=False, msg_count=messages)

for i in range(messages):
    print('Topic: ', m[i].topic) #토픽
    print('Message: ', m[i].payload.decode()) #메시지
