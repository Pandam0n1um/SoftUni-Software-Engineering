import sys
count_numbers = int(input())

max_even_number = -sys.maxsize - 1
min_even_number = sys.maxsize
even_sum = 0

max_odd_number = -sys.maxsize - 1
min_odd_number = sys.maxsize
odd_sum = 0

for number in range(1, count_numbers + 1):
    new_number = float(input())
    if not number % 2 == 0:
        odd_sum+=new_number
        if new_number>max_odd_number:
           max_odd_number=new_number
        if new_number<min_odd_number:
            min_odd_number=new_number
    else:
        even_sum+=new_number
        if new_number>max_even_number:
           max_even_number=new_number
        if new_number<min_even_number:
            min_even_number=new_number

print(f"OddSum={odd_sum:.2f},")
if count_numbers<1:
    print(f"OddMin=No,")
else:
    print(f"OddMin={min_odd_number:.2f},")

if count_numbers<1:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_odd_number:.2f},")

print(f"EvenSum={even_sum:.2f},")

if count_numbers<2:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={min_even_number:.2f},")

if count_numbers<2:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={max_even_number:.2f}")
