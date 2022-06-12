def number_increment(numbers):
	def increase():
		return [number + 1 for number in numbers]

	return increase()

# a=5
print(number_increment([1, 2, 3]))
#
# print(func())
# print('blank')
# print(number_increment([1, 2, 3]))
