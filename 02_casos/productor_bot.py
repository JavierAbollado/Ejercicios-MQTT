from paho.mqtt.client import Client

from time import sleep
from random import random

def main(broker, topic):
    client = Client()

    client.connect(broker)
    client.loop_start()

    print('publishing')
    cont = 0
    while True:
        data  = str(cont)
        client.publish(topic,  data)
        print('.', end= '', flush=True)
        sleep(random()*3)
        cont += 1


if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
    broker = sys.argv[1]
    topic = sys.argv[2]
    main(broker, topic)
