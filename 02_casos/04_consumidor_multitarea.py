from paho.mqtt.client import Client
from time import sleep

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)


def main(broker, topics):
    client = Client()
    client.on_message = on_message

    print(f'Connecting on channels {topics} on {broker}')
    client.connect(broker)

    for t in topics:
        client.subscribe(t)


    client.loop_start()

    for i in range(50):
        print ('.', end=" ", flush=True)
        sleep(1)

    client.disconnect()
    print ('end')



if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
    broker = sys.argv[1]
    topics = sys.argv[2:]
    main(broker, topics)
