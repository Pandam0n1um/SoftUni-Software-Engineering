# from collections import deque
#
# working_bees = deque([int(bee) for bee in input().split()])
# nectar = [int(x) for x in input().split()]
# signs = input().split()


from collections import deque


def calculation(bee, nectar, symbol):
	result = 0
	if symbol == '+':
		result = bee + nectar
	elif symbol == "-":
		result = bee - nectar

	elif symbol == "*":
		result = bee * nectar

	# elif symbol == "/":   Problem  if nectar = 0
	elif symbol == "/" and nectar > 0:
		result = bee / nectar
	return abs(result)


bees_deque = deque(int(x) for x in input().split())
nectar_stack = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while bees_deque and nectar_stack:
	bee_value = bees_deque.popleft()
	nectar_value = nectar_stack.pop()

	if nectar_value < bee_value:
		bees_deque.appendleft(bee_value)
		continue
	elif symbols:
		symbol = symbols.popleft()
		honey = calculation(bee_value, nectar_value, symbol)
		total_honey += honey

print(f"Total honey made: {total_honey}")
if bees_deque:
	print(f'Bees left: {", ".join([str(x) for x in bees_deque])}')
if nectar_stack:
	print(f'Nectar left: {", ".join([str(x) for x in nectar_stack])}')