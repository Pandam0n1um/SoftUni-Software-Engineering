input_info = str(input())

sum_money = 0

while not input_info == str("NoMoreMoney"):
    input_money = float(input_info)
    if input_money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {input_money:.2f}")
    sum_money += input_money
    input_info = str(input())

print(f"Total: {sum_money:.2f}")
