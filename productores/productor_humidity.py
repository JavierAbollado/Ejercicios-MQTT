from paho.mqtt.client import Client

from time import sleep
from random import random,randint
import sys


def main(hostname):
    client = Client()

    client.username_pw_set('hygrometer', password=None)
    client.connect(hostname)
    #client.connect("localhost")
    client.loop_start()

    #topic = input('topic? ')
    print('publishing')
    cont = 0
    low = 20
    while True:
        data  = str(low+cont+randint(-5,5))
        client.publish('humidity',  data)
        print('.', end= '', flush=True)
        sleep(random()*3)
        cont = (cont + 1) % 80

if __name__ == '__main__':
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
