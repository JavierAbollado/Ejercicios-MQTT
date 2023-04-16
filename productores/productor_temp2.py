from paho.mqtt.client import Client

from time import sleep
from random import random
import sys

def main(hostname):
    client = Client()

    client.connect(hostname)
    #client.connect("localhost")
    client.loop_start()

    topic = input('topic? ')
    print('publishing')
    cont = 0
    while True:
        data  = str(cont)
        client.publish(topic,  data)
        print('.', end= '', flush=True)
        sleep(random()*3)
        cont += 1


if __name__ == '__main__':
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
