from paho.mqtt.client import Client

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    if msg.payload == b'adios':
        print ('unsubscribe', msg.topic)
        client.unsubscribe(msg.topic)
    elif msg.payload == b'next':
        new = chr(ord(msg.topic[-1])+1)
        print (f'subscribe also "/clients/{new}"')
        client.subscribe(f"/clients/{new}")

def main(broker, topics):
    client = Client()
    client.on_message = on_message

    print(f'Connecting on channels {topics} on {broker}')
    client.connect(broker)

    for t in topics:
        client.subscribe(t)

    client.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
    broker = sys.argv[1]
    topics = sys.argv[2:]
    main(broker, topics)
