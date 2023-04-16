from paho.mqtt.client import Client

client = Client()

client.connect("picluster02.mat.ucm.es")

topic = input('topic? ')
while True:
    data  = input('message?')
    client.publish(topic,  data)
