from paho.mqtt.client import Client 

client = Client()

client.connect("localhost")
client.loop_start()

topic = input('topic? ')
while True:
    data  = input('message?')
    client.publish(topic,  data)
