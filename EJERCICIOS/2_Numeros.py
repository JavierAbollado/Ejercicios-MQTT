from paho.mqtt.client import Client
import traceback
import sys


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    
    try:
        n =  float(msg.payload)
        if n % 1 == 0:
            userdata['n_enteros'] += 1
            client.publish('/clients/n_enteros', f'{userdata["n_enteros"]}')
            client.publish('/clients/enteros', n)
        else:
            userdata['frec_reales'] += 1
            client.publish('/clients/n_reales', f'{userdata["n_reales"]}')
            client.publish('/clients/reales', n)
    
    except ValueError:
        pass
    
    except Exception as e:
        raise e


def main(broker):
    userdata = {
        'n_enteros': 0,
        'n_reales':0
    }
    client = Client(userdata=userdata)
    client.on_message = on_message
    
    print(f'Connecting on channels numbers on {broker}')
    client.connect(broker)
    
    client.subscribe('Numbers')
    client.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
