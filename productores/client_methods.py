#!/usr/bin/python
# -*- coding: utf-8 -*-

from paho.mqtt.client import Client

def on_connect(mqttc, userdata, flags, rc):
    print("CONNECT:", userdata, flags, rc)

def on_message(mqttc, userdata, msg):
    print("MESSAGE:", userdata, msg.topic, msg.qos, msg.payload, msg.retain)
    #mqttc.publish('clients/propio', msg.payload)

def on_publish(mqttc, userdata, mid):
    print("PUBLISH:", userdata, mid)

def on_subscribe(mqttc, userdata, mid, granted_qos):
    print("SUBSCRIBED:", userdata, mid, granted_qos)

def on_log(mqttc, userdata, level, string):
    print("LOG", userdata, level, string)

mqttc = Client(userdata="data (of any type) for user")
mqttc.enable_logger()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
#mqttc.on_log = on_log

#mqttc.connect("localhost")
#mqttc.username_pw_set('carlos', password=None)
mqttc.connect("simba.fdi.ucm.es")

topic = input('topic? ')
mqttc.subscribe(topic)

mqttc.loop_forever()
