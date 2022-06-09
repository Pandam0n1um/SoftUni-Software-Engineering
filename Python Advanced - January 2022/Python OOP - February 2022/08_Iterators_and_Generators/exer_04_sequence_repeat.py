class sequence_repeat:
	def __init__(self, sequence: list, number: int):
		self.sequence = sequence
		self.number = number
		self.pos = 0
		self.adjuster = len(self.sequence)

	def __iter__(self):
		return self

	def __next__(self):
		if self.pos >= self.number:
			raise StopIteration
		result = self.sequence[self.pos % self.adjuster]
		self.pos += 1
		return result


result = sequence_repeat('abcdefghijklmnopqrst', 2)
for item in result:
	print(item, end='')
