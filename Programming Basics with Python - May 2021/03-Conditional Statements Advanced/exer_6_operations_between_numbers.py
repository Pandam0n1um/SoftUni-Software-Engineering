number_1 = int(input())

number_2 = int(input())

operator = str(input())

result = None

if operator == str("+") or operator == str("-") or operator == str("*"):
    if operator == str("+"):
        result = (number_1 + number_2)
    elif operator == str("-"):
        result = (number_1 - number_2)
    elif operator == str("*"):
        result = (number_1 * number_2)

    if result % 2 == 0:
        print(f"{number_1} {operator} {number_2} = {result} - even")
    else:
        print(f"{number_1} {operator} {number_2} = {result} - odd")

elif operator == str("/"):
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        result = (number_1 / number_2)
        print(f"{number_1} {operator} {number_2} = {result:.2f}")
elif operator == str("%"):
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        remainder = (number_1 % number_2)
        print(f"{number_1} {operator} {number_2} = {remainder}")
