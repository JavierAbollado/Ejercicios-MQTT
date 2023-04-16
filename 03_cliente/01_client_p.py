from paho.mqtt.client import Client

def main(broker, topic):
    client = Client()

    #client.connect("localhost")
    #client.connect("iot.eclipse.org")
    print(f'connecting {broker}...', end='')
    client.connect(broker)
    print('OK.')
    client.loop_start()

    while True:
        data  = input('message?')
        print(f'publishing {data} on {topic}')
        client.publish(topic,  data)


if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
        sys.exit(1)
    broker = sys.argv[1]
    topic= sys.argv[2]
    main(broker, topic)
