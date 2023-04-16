import paho.mqtt.publish as publish
import sys

def main(hostname):
    topic = input('topic? ')
    data  = input('message? ')

    publish.single(topic, payload=data,
                   hostname=hostname)

if __name__ == "__main__":
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
