'''import paho.mqtt.client as mqtt
import ssl
import os
import json

# AWS IoT Core 엔드포인트
AWS_IOT_ENDPOINT = 'a3j29icjdebdp7-ats.iot.ap-northeast-2.amazonaws.com'

# 인증서 및 키 파일 경로 (절대 경로로 수정)
CA_CERT_PATH = 'AmazonRootCA1.pem'
CERT_FILE_PATH = 'certificate.pem.crt'
KEY_FILE_PATH = 'private.pem.key'

# MQTT 주제와 메시지
TOPIC = 'topic_2'
MESSAGE = 'Dongmin'
with open('send.json','r') as f:
    MESSAGE = json.load(f)
# MQTT 클라이언트 콜백 함수
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 연결 후 메시지 발행
    print(f"Message '{MESSAGE}' published to topic '{TOPIC}'")
def on_message(client, userdata, msg):
    data= json.loads(msg.payload.decode())
    with open('get.json','w') as f:
        json.dump(data,f)
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

# MQTT 클라이언트 생성
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 클라이언트 인증 설정
client.tls_set(ca_certs=CA_CERT_PATH,
               certfile=CERT_FILE_PATH,
               keyfile=KEY_FILE_PATH,
               tls_version=ssl.PROTOCOL_TLSv1_2)

client.on_connect = on_connect
client.on_message = on_message
# 서버에 연결
client.connect(AWS_IOT_ENDPOINT, port=8883, keepalive=60)

client.publish(TOPIC, MESSAGE)

'''

import paho.mqtt.client as mqtt
import ssl
import os
import json

# AWS IoT Core 엔드포인트
AWS_IOT_ENDPOINT = 'a3j29icjdebdp7-ats.iot.ap-northeast-2.amazonaws.com'

# 인증서 및 키 파일 경로 (절대 경로로 수정)
CA_CERT_PATH = 'AmazonRootCA1.pem'
CERT_FILE_PATH = 'certificate.pem.crt'
KEY_FILE_PATH = 'private.pem.key'

# MQTT 주제와 메시지
TOPIC = 'topic_1'
MESSAGE = 'Bo Seong Big man'

# MQTT 클라이언트 콜백 함수
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 연결 후 메시지 발행
    #client.publish(TOPIC, MESSAGE)
    #print(f"Message '{MESSAGE}' published to topic '{TOPIC}'")


def on_message(client, userdata, msg):
    data= json.loads(msg.payload.decode())
    with open('get.json','w') as f:
        json.dump(data,f)
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

# MQTT 클라이언트 생성

# 클라이언트 인증 설정
client.tls_set(ca_certs=CA_CERT_PATH,
               certfile=CERT_FILE_PATH,
               keyfile=KEY_FILE_PATH,
               tls_version=ssl.PROTOCOL_TLSv1_2)



# 서버에 연결
client.connect(AWS_IOT_ENDPOINT, port=8883, keepalive=60)

# 메시지 구독

# 메시지 수신 대기
#client.loop_forever(timeout=5)

client.publish('topic_2',"Dongmin")