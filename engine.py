import thread
from queue import eventQueue

class eventEngine:
	q = eventQueue()

	eventHandlers = []

	def addHandler(self, handlers):
		self.eventHandlers.extend(handlers)

	def pushEvent(self, event):
		self.q.push(event)

	def main(self, q, eventHandlers):
		done = False
		while not done:
			currEvent = q.pop()
			for h in eventHandlers:
				print currEvent
				if currEvent.id == "terminate":
					done = True
				elif currEvent.id == h.id:
					try:
						h.run(currEvent)
					except:
						h.default()

	def init(self):
		thread.start_new_thread(self.main, (self.q, self.eventHandlers))

class eventHandler:
	id = ""
	def default(self):
		print "no function defined"

