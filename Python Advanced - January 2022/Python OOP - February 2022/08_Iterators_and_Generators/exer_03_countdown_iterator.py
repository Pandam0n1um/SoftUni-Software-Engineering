class countdown_iterator:
	def __init__(self, count: int):
		self.count = count
		self.end = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.count < self.end:
			raise StopIteration
		result = self.count
		self.count -= 1
		return result


iterator = countdown_iterator(10)
for item in iterator:
	print(item, end=" ")

print()

iterator = countdown_iterator(-10)
for item in iterator:
	print(item, end=" ")

print()

iterator = countdown_iterator(110)
for item in iterator:
	print(item, end=" ")