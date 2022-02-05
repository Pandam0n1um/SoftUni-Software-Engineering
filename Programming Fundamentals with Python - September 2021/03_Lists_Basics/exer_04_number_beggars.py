beggar_income_string = input()

beggar_count = int(input())

beggar_income_list = beggar_income_string.split(", ")

sum_gathered = [0] * beggar_count

iteration_count = 0

is_complete = False

while not is_complete:
    for income in range(beggar_count):
        if iteration_count == len(beggar_income_list):
            is_complete = True
            break
        sum_gathered[income] += int(beggar_income_list[iteration_count])
        iteration_count += 1

print(sum_gathered)
