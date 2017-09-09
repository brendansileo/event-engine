class eventQueue:
	events = []
	numEvents = 0

	def push(self, event):
		self.events.append(event)
		self.numEvents+=1;

	def pop(self):
		self.numEvents-=1;
		return self.events.pop(0)

	def getLen(self):
		return self.numEvents