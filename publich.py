import paho.mqtt.client as mqtt #import the client1
from datetime import datetime

def publish(client,topic, message, qos=0, retain=False):
  client.publish(topic, message, qos=qos, retain=retain)


message="Hello - teste Mqtt"
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
message = f"{message} ({timestamp})"
broker_address="broker.hivemq.com"
print("creating new instance")
client = mqtt.Client("Turma IOT" )
print("connecting to broker")
client.connect(broker_address, 1883,60) 
client.publish("temperaturauniso",22,qos=0)
publish(client,"sla", "asdasd", qos=2, retain=True)
publish(client, "UNISOTOP", "asdasdasd- 1 ", qos=0, retain=False)
publish(client, "UNISOTOP", "Teste Mqtt - 2 ", qos=1, retain=False)
publish(client, "UNISOTOP", "Teste Mqtt - 3 ", qos=2, retain=False)