from paho.mqtt.client import Client
import sys
import time

def main(broker, tiempo_espera, topic, mensaje):

    # guardar datos y pasarlos al Client
    userdata = {
        'tiempo_espera':tiempo_espera, 
        'topic':topic,
        'mensaje': mensaje
    }
    client = Client(userdata=userdata)
    print(f'Connecting on channels numbers on {broker}')

    # conectarnos, esperar y publicar
    client.connect(broker)
    time.sleep(float(userdata['tiempo_espera']))
    client.publish(userdata['topic'], userdata['mensaje'])


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} broker topic topic_p")
        sys.exit(1)
    broker = sys.argv[1]
    tiempo_espera = sys.argv[2]
    topic = sys.argv[3]
    mensaje = sys.argv[4]
    main(broker, tiempo_espera, topic, mensaje)
