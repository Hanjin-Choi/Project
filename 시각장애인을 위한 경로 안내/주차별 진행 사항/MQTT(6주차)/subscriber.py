import paho.mqtt.client as mqtt
import json
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("mqtt/myiot/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data= json.loads(msg.payload.decode())
    with open('get.json','w') as f:
        json.dump(data,f)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("70.12.108.91", 1883, 60)
client.loop_forever()