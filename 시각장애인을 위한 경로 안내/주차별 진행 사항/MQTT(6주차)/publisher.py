import paho.mqtt.client as mqtt
import json
data = json.load('get.json')
#MQTT 클라이언트 생성, 이름은 mypub
mqtt = mqtt.Client("mypub")
#로컬호스트에 있는 MQTT 서버에 TCP 1883 포트로 접속
mqtt.connect("70.12.108.91", 1883)

#토픽에 메세지 발행
mqtt.publish("mqtt/myiot/paho", data)
print("The message is published.")
mqtt.loop(2)