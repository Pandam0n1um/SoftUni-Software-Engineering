class take_skip:
	def __init__(self, step: int, count: int):
		self.step = step
		self.count = count
		self.element = 0
		self.passed_iterations = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.passed_iterations >= self.count:
			raise StopIteration

		result = self.element
		self.passed_iterations += 1
		self.element += self.step
		return result


numbers = take_skip(2, 6)
for number in numbers:
	print(number)
numbers = take_skip(10, 5)
for number in numbers:
	print(number)
