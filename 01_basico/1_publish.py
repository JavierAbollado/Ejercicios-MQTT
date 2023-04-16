import paho.mqtt.publish as publish
import sys

def main(hostname):
    topic = '/clients/prueba'
    while True:
        data  = input('message? ')
        print(f"Publishing {data} in :{topic}:")
        publish.single(topic,  data, hostname=hostname)

if __name__ == "__main__":
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
