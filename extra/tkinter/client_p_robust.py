from paho.mqtt.client import Client

client = Client()

client.connect("picluster02.mat.ucm.es")
client.loop_start()

topic = "clients/tkinter"
while True:
    data  = input('message?')
    client.publish(topic,  data)
