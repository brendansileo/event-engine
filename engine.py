import thread
from queue import eventQueue

class eventEngine:
	q = eventQueue()

	eventHandlers = []

	def addHandler(handler):
		eventHandlers.append(handler)

	def main(q, eventHandlers):
		done = False
		while not done:
			if q.getLen() != 0:
				currEvent = q.pop()
				for h in eventHandlers:
					if currEvent.id == "terminate":
						done = True
					else if currEvent.id == h.id:
						try:
							h.run(currEvent)
						except:
							h.default()

	def init():
		thread.start_new_thread(main, [q, eventHandlers])

class eventHandler:
	id = ""
	def default():
		print "no function defined"