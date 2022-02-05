# numbers_list = [int(i) for i in input().split()]
#
# min_value=min(numbers_list)
# max_value=max(numbers_list)
# sum_value=sum(numbers_list)
#
# print(f"The minimum number is {min_value}")
# print(f"The maximum number is {max_value}")
# print(f"The sum number is: {sum_value}")

def min_num(nums):
    sum_of_digits = []
    for n in nums:
        sum_of_digits.append(int(n))
    return min(nums), max(nums), sum(sum_of_digits)


numbers = input().split()
minimum, maximum, sums = min_num(numbers)
print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {sums}")
print(type(sums))