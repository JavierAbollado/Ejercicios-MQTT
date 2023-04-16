import paho.mqtt.subscribe as subscribe
import sys

def main(hostname):
    topic = '/clients/prueba'
    n_msg = int(input('number of messages? '))

    print(f"Subcribing :{topic}:, {n_msg} messages")
    msgs = subscribe.simple(topic,
                            msg_count = n_msg,
                            hostname = hostname)

    if n_msg == 1:
        print(msgs.topic, msgs.payload.decode('utf8'))
    else:
        for m in msgs:
            print(m.topic, m.payload.decode('utf8'))

if __name__ == "__main__":
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
