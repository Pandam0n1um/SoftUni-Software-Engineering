def add(sequence: set, new_values: list):
	return sequence.update(new_values)


def remove(sequence: set, new_values: list):
	return sequence.difference(new_values)


def check_subset():
	if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
		return True
	return False


first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

lines_count = int(input())

set_order = {'First': first_sequence, 'Second': second_sequence}

for i in range(lines_count):
	action, position, *number_values = input().split()
	number_values = set([int(x) for x in number_values])

	if action == 'Add':
		add(set_order[position],number_values)
	elif action == 'Remove':
		set_order[position]=remove(set_order[position],number_values)
	elif action == 'Check':
		print(check_subset())


for values in set_order.values():
	print(', '.join([str(num) for num in sorted(values)]))



# print(', '.join(sorted(first_sequence)))
# print(', '.join(sorted(second_sequence)))

