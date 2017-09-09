#!/usr/bin/env python
from engine import eventEngine, eventHandler

e = eventEngine()

def testHandler(self, event):
	print event["text"]

e.addHandler("say", testHandler)
e.init()


done = False
while not done:
	i = raw_input(">")
	if i.split()[0] == "say":
		e.pushEvent({"id":"say", "text":i[4:]})
	else:
		e.pushEvent({"id":"terminate"})
		done = True