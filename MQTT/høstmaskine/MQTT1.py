import paho.mqtt.client as mqtt
import database1


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))
    client.subscribe("trek/22/bathroom/#")
    client.subscribe("trek/22/bedroom/#")
    client.subscribe("trek/22/kitchen/#")
    client.subscribe("trek/22/test")
    client.subscribe("trek/22/sensor")
    client.subscribe("trek/22/#")
    client.subscribe("trek/22/+")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    database1.insert(str(msg.topic),str(msg.payload,'UTF-8'))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
#client.connect("10.100.0.96", 1883, 60)
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
