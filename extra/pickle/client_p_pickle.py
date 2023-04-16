from paho.mqtt.client import Client
import pickle

client = Client()

client.connect("picluster02.mat.ucm.es")
client.loop_start()

topic = input('topic? ')
while True:
    data  = input('message?')
    client.publish(topic,  pickle.dumps(eval(data)))
