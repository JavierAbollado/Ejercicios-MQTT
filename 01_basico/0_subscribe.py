import paho.mqtt.subscribe as subscribe
import sys

def main(hostname):
    topic = input('topic? ')

    msg = subscribe.simple(topic,
                           hostname=hostname)

    print(msg.topic, msg.payload, msg.payload.decode('utf8'))

if __name__ == "__main__":
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
