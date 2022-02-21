from collections import deque

MAIN_COLORS = ('red', 'yellow', 'blue')
SECONDARY_COLORS = ('orange', 'purple', 'green')
REQUIRED_COLORS = {
	'orange',
	'purple',
	'green'
}

collected_colors = []

substrings = deque(input().split())

while substrings:
	first_substring = substrings.popleft()
	second_substring = substrings.pop() if substrings else ''

	result = first_substring + second_substring
	if result in MAIN_COLORS or result in SECONDARY_COLORS:
		collected_colors.append(result)
		continue

	result = second_substring + first_substring
	if result in MAIN_COLORS or result in SECONDARY_COLORS:
		collected_colors.append(result)
		continue

	first_substring = first_substring[:-1]
	second_substring = second_substring[:-1]

	if first_substring:
		substrings.insert(len(substrings) // 2, first_substring)

	if second_substring:
		substrings.insert(len(substrings) // 2, second_substring)

result = []

for color in collected_colors:
	if color in MAIN_COLORS:
		result.append(color)
	else:
		pass

print(substrings)
