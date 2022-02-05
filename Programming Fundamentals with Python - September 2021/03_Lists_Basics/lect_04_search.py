n_string = int(input())
keyword = input()

total_list = []
softuni_list = []

for _ in range(n_string):
    current_string = input()
    total_list.append(current_string)
    if keyword in current_string:
        softuni_list.append(current_string)

print(total_list)
print(softuni_list)