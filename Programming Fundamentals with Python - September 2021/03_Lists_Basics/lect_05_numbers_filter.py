lines_count = int(input())

even_values = []
odd_values = []
positive_values = []
negative_values = []

for _ in range(lines_count):
    current_value = int(input())
    if current_value >= 0:
        positive_values.append(current_value)
    if current_value < 0:
        negative_values.append(current_value)
    if current_value % 2 == 0:
        even_values.append(current_value)
    if current_value % 2 == 1:
        odd_values.append(current_value)
command = input()

if command == "even":
    print(even_values)
elif command == "odd":
    print(odd_values)
elif command == "positive":
    print(positive_values)
else :
    print(negative_values)
