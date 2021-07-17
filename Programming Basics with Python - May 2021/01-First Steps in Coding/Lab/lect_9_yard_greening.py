yardarea = float(input())

initial_price = float(yardarea * 7.61)
discount = float(initial_price * 0.18)
final_price = float(initial_price - discount)

print(f'The final price is:{final_price} lv.')
print(f'The discount is:{discount} lv.')
