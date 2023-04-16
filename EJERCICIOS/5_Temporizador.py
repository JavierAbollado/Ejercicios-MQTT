from paho.mqtt.client import Client
from multiprocessing import Process
import time

TOPIC = "clients/cualquiertopic"

def timer(mqttc,msg):
    data = msg.payload.split(",") # Recibe : "tiempo,topic,mensaje" -> Devuelve : ["tiempo", "topic", "mensaje"]
    time.sleep(float(data[0]))
    mqttc.publish(data[1], data[2])

def on_message(mqttc, data, msg):
    try:
        p = Process(target=timer, args=(mqttc, msg)) 
        p.start()
    except Exception as e:
        print(e)
    
def on_log(mqttc, userdata, level, string):
    print("LOG", userdata, level, string)
    
def main(broker):
    userdata={'status' : 0}
    mqttc = Client(userdata=userdata)
    mqttc.enable_logger()
    mqttc.on_message = on_message
    mqttc.on_log = on_log
    mqttc.connect(broker)
    mqttc.subscribe(TOPIC)
    mqttc.pub
    mqttc.loop_forever
    
if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
        sys.exit(1)
    broker = sys.argv[1]
    main(broker)
