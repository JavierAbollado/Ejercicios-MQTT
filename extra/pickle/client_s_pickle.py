from paho.mqtt.client import Client
import pickle

def on_message(client, userdata, msg):
    data = pickle.loads(msg.payload)
    print(msg.topic, data, type(data))


client = Client()
client.on_message = on_message

client.connect("picluster02.mat.ucm.es")
topic = input('topic? ')
client.subscribe(topic)

client.loop_forever()
