def odd_even_sum(init_value):
    odd_sum = 0
    even_sum = 0
    digits_list = [int(i) for i in init_value]

    for num in range(len(digits_list)):
        if digits_list[num] % 2 == 0:
            even_sum += digits_list[num]
        else:
            odd_sum += digits_list[num]
    return odd_sum, even_sum

    # for num in range(len)


initial_value = input()

result = odd_even_sum(initial_value)

print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
