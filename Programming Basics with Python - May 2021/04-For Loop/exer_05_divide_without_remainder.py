numbers_amount = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0

for number in range(numbers_amount):
    number_input = int(input())
    if number_input % 2 == 0:
        p1_counter += 1
    if number_input % 3 == 0:
        p2_counter += 1
    if number_input % 4 == 0:
        p3_counter += 1

ratio_p1=(p1_counter/numbers_amount)*100
ratio_p2=(p2_counter/numbers_amount)*100
ratio_p3=(p3_counter/numbers_amount)*100

print(f"{ratio_p1:.2f}%")
print(f"{ratio_p2:.2f}%")
print(f"{ratio_p3:.2f}%")