from paho.mqtt.client import Client

from time import sleep
from random import random, randint
import sys


def main(hostname):
    client = Client()
    client.username_pw_set('thermometer', password=None)
    client.connect(hostname)
    #client.connect("localhost")
    client.loop_start()

    #topic = input('topic? ')
    print('publishing')
    cont = 0
    while True:
        data  = str(cont)
        data2 = str(cont+randint(-2,2))
        client.publish('temperature/t1',  data)
        client.publish('temperature/t2',  data2)
        print('.', end= '', flush=True)
        sleep(random()*3)
        cont = (cont + 1) % 40



if __name__ == '__main__':
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
