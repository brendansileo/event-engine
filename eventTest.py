from engine import eventEngine, eventHandler

def testHandler(self, event):
	print "this was a test"



e = eventEngine()

e.addHandler("test", testHandler)
e.init()
e.pushEvent({"id":"test"})
e.pushEvent({"id":"terminate"})