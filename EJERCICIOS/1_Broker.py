from paho.mqtt.client import Client
import sys


def on_message(client, userdata, m):
    print("MESSAGE: ", userdata, m.topic, m.qos, m.payload, m.retain)
    client.publish('clients/pruebas', m.payload)

def main(broker, topic):
    client = Client()
    client.on_message = on_message
    client.connect(broker) 
    client.subscribe(topic)
    client.loop_forever()

if __name__ == "__main__":
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
        sys.exit(1)
    # pasar como argumentos en la consola el broker y el topic
    broker = sys.argv[1]
    topic = sys.argv[2]
    main(broker, topic)
