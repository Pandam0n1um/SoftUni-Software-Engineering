def calculation(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2


oper = input()
number_1 = int(input())
number_2 = int(input())

print(calculation(operator=oper, num_2=number_2, num_1=number_1))