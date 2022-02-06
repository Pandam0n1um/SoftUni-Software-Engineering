numbers_list = [int(i) for i in input().split(", ")]

even_numbers = [str(n) for n in numbers_list if n % 2 == 0]
odd_numbers = [str(n) for n in numbers_list if not n % 2 == 0]
positive_numbers = [str(n) for n in numbers_list if 0 <= n]
negative_numbers = [str(n) for n in numbers_list if n < 0]

print("Positive: "+", ".join(positive_numbers))
print("Negative: "+", ".join(negative_numbers))
print("Even: "+", ".join(even_numbers))
print("Odd: "+", ".join(odd_numbers))



# even_numbers = list(filter(lambda number: number % 2 == 0, numbers_list))
# odd_numbers = list(filter(lambda number: not number % 2 == 0, numbers_list))
# positive_numbers = list(filter(lambda number: number >= 0, numbers_list))
# negative_numbers = list(filter(lambda number: number < 0, numbers_list))


# positive_numbers_str="Positive: "+", ".join(positive_numbers)
# negative_numbers_str="Negative: "+", ".join(negative_numbers)
# even_numbers_str="Even: "+", ".join(even_numbers)
# odd_numbers_str="Odd: "+", ".join(odd_numbers)