
"""
	Semaphore.
	Execution order with restriction for 2 processes.
"""

class Mutex:
	def __init__(self):
		self.ready = Queue()
		self.status = 0

	def wait(self, func):
		if self.status == 0:
			func()
			self.ready.dequeue()
			self.status = 1
		else:
			self.ready.enqueue(func)

	def signal(self):
		self.ready.dequeue()
		self.status = 0


class Queue:
	def __init__(self):
		self.queue = list()

	def enqueue(self, func):
		self.queue.append(func)

	def dequeue(self):
		if self.queue:
			func = self.queue[0]
			self.queue = self.queue[1:]
			func()
