from paho.mqtt.client import Client

from time import sleep
from random import random,randint
import sys


def main(hostname):

    client = Client()

    client.username_pw_set('num_generator', password=None)
    client.connect(hostname)
    #client.connect("localhost")
    client.loop_start()

    #topic = input('topic? ')
    print('publishing')

    while True:
        if randint(0,1):
            data = randint(0,99)
        else:
            data = random()
        data  = str(data)
        client.publish('numbers',  data)
        print('.', end= '', flush=True)
        sleep(random()*3)


if __name__ == '__main__':
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
