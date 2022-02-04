number_str = input()
largest_num = ""

for n in range(9, -1, -1):
    for i in number_str:
        if i == str(n):
            largest_num += str(i)
print(largest_num)

number = list(input())

number.sort(reverse=True)

print("".join(number))




