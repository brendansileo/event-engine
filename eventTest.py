from engine import eventEngine, eventHandler

e = eventEngine()

def testHandler(self, event):
	print "this was a test"

e.addHandler("test", testHandler)
e.init()

e.pushEvent({"id":"test"})
e.pushEvent({"id":"terminate"})