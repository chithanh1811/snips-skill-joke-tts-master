#!/usr/bin/env python3

#- * -coding: utf - 8 - * -

from hermes_python.hermes import Hermes
import requests
import json
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

with open('jokes.json') as json_file:
    joke = json.load(json_file)["jokes"][random.randint(0, joke["count"])]

def intent_received(hermes, intent_message):
    if joke["type"] == "single":
        sentence = joke["joke"]
    else:
        sentence = joke["setup"] + "      " + joke["delivery"]
    hermes.publish_end_session(intent_message.session_id, sentence)
    print(sentence)
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
