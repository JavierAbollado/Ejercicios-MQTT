from paho.mqtt.client import Client
import traceback
import sys


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    try:
        n =  int(msg.payload)
        userdata['suma'] += n
        client.publish('/clients/suma', f'{userdata["suma"]}')
        if n % 2 == 0:
            client.publish('/clients/par', msg.payload)
        else:
            client.publish('/clients/impar', msg.payload)
    except ValueError:
        pass
    except Exception as e:
        raise e


def main(broker):
    userdata = {'suma':0}
    client = Client(userdata=userdata)
    client.on_message = on_message

    print(f'Connecting on channels numbers on {broker}')
    client.connect(broker)

    client.subscribe('numbers')

    client.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
