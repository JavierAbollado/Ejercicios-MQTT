from paho.mqtt.client import Client


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)


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
