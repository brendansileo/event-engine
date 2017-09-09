import threading
from queue import eventQueue
from types import MethodType

class eventEngine:
	q = eventQueue()

	eventHandlers = []

	def addHandler(self, newId, function):
		self.eventHandlers.append(eventHandler(newId, function))

	def pushEvent(self, event):
		self.q.push(event)

	def main(self, q, eventHandlers):
		done = False
		while not done:
			try:
				currEvent = q.pop()
				for h in eventHandlers:
					if currEvent["id"] == "terminate":
						done = True
					elif currEvent["id"] == h.id:
						#try:
						h.run(currEvent)
						#except:
						#	h.default()
			except IndexError:
				pass

	def init(self):
		t=threading.Thread(target=self.main, args=(self.q, self.eventHandlers))
		t.start()

class eventHandler:
	id = ""
	@classmethod
	def default(self):
		print "no function defined"

	def __init__(self, newId, function):
		self.id = newId
		self.run = MethodType(function, self, eventHandler)

