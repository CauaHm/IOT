import paho.mqtt.client as mqtt #import the client1



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("UNISOTOP", qos=0)

def on_message(client, userdata, message):
    print(f"Message received on topic {message.topic}: {message.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60) 
client.loop_forever()