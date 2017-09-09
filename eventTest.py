from engine import eventEngine, eventHandler

class testHandler(eventHandler):
	id="test"
	def run():
		print "this was a test"

e = eventEngine()

e.addHandler([testHandler])
e.init()

while True:
	e.pushEvent({"id":"test"})