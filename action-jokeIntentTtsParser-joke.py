#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import json
import requests

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

joke = requests.get("https://sv443.net/jokeapi/category/Any").json()



def intent_received(hermes, intent_message):
	if joke["type"] == "single":
    	sentence = joke["joke"]

	if joke["type"] == "twopart":
	    sentence = joke["setup"] + "          " joke["delivery"]
    hermes.publish_end_session(intent_message.session_id, sentence)

with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
