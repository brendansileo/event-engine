class eventQueue:
	events = []
	numEvents = 0

	def push(event):
		events.append(event)
		numEvents+=1;

	def pop():
		numEvents-=1;
		return events.pop(0)