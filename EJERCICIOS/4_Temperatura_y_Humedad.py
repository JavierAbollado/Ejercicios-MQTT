from paho.mqtt.client import Client
import sys

# valores arbitrarios
K0 = 15
K1 = 50

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    n = float (msg.payload)

    if msg.topic == 'temperature/t1':
        if n > K0 and not userdata['reading_humidity']:
            client.subscribe('humidity')
            userdata['reading_humidity'] = True
        elif n < K0 and userdata['reading_humidity']:
            client.unsubscribe('humidity')
            userdata['reading_humidity'] = False

    if msg.topic == 'humidity':
        if n > K1:
            client.unsubscribe('humidity')
            userdata['reading_humidity'] = False

def main(broker):
    userdata = {
        'reading_humidity':False
    }
    client = Client(userdata= userdata)
    client.on_message = on_message

    print(f'Connecting on channels numbers on {broker}')
    client.connect(broker)

    client.subscribe('temperature/t1')

    client.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
