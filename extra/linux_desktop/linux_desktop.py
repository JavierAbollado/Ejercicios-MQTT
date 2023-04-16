#Cliente de mqtt conectado con el sistema de notifiaciones de ubuntu.

from paho.mqtt.client import Client
import notify2

notify2.init('MQTT')

def on_message(client, userdata, msg):
    print(client, userdata, msg.topic, msg.payload)
    #los mensajes recibidos son enviados a ubuntu
    notify2.Notification(msg.topic, msg.payload).show()

client = Client()
client.on_message = on_message

client.connect("picluster02.mat.ucm.es")
topic = input('topic? ')
client.subscribe(topic)

client.loop_forever()
