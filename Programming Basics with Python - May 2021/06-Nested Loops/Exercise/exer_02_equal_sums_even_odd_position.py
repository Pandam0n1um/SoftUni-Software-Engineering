num_1=int(input())
num_2=int(input())

for number in range(num_1, num_2 + 1):
    number_to_str=str(number)
    sum_odd_positions=0
    sum_even_positions=0
    for index, digit in enumerate(number_to_str):
        if index%2==0:
            sum_even_positions+=int(digit)
        else:
            sum_odd_positions+=int(digit)
    if sum_even_positions==sum_odd_positions:
        print(f"{number} ", end="")