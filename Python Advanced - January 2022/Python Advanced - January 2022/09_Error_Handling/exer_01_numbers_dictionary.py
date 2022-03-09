numbers_dictionary = {}

while True:
	line = input()
	if line == "Search":
		break
	number_as_string = line
	try:
		number = int(input())
		numbers_dictionary[number_as_string] = number
	except ValueError:
		print("The variable number must be an integer")

while True:
	line = input()
	if line == "Remove":
		break
	searched = line
	try:
		print(numbers_dictionary[searched])
	except KeyError:
		print("Number does not exist in dictionary")

while True:
	line = input()
	if line == "End":
		break
	searched = line
	try:
		numbers_dictionary.pop(searched)
	except KeyError:
		print("Number does not exist in dictionary")

print(numbers_dictionary)
