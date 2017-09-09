from engine import eventEngine, eventHandler

class testHandler(eventHandler):
	id="test"
	@classmethod
	def run(self, event):
		print "this was a test"

e = eventEngine()

e.addHandler([testHandler])
e.init()
e.pushEvent({"id":"test"})
e.pushEvent({"id":"terminate"})