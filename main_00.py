import sync_00 as s0

mutex = s0.Mutex()

def hello():
	print('hello')

def printname(name):
	print(name)

def later():
	mutex.wait(lambda: printname('ivan') )

def first():
	hello()
	mutex.signal()

first()
later()

later()
later()
later()

first()
first()
first()

first()
