# numbers_list = [int(i) for i in input().split(", ")]
#
# max_limit = 10
# while len(numbers_list) > 0:
#     group = [x for x in numbers_list if max_limit - 10 < x <= max_limit]
#     print(f"Group of {max_limit}'s: {group}")
#     for elem in group:
#         numbers_list=[i for i in numbers_list if not i==elem]
#     max_limit+=10


# numbers = input().split(", ")
#
# removing = numbers.copy()  # Copy the list, so we can safely remove items
# step = 10  # Step for every iteration, to have groups for 10's, 20's, 30's... etc.
# while len(removing) > 0:
#     my_list = []
#     for nums in numbers:
#         if step-10<int(nums) <= step:
#             my_list.append(int(nums))
#             removing.remove(nums)
#     print(f"Group of {step}'s: {my_list}")
#     step += 10
# # print(id(numbers))


numbers = input().split(", ")

removing = numbers.copy()  # Copy the list, so we can safely remove items
step = 10  # Step for every iteration, to have groups for 10's, 20's, 30's... etc.
print(id(numbers))
print(id(removing))
print("while loop starts")
while len(removing) > 0:
    my_list = []
    for nums in numbers:
        if int(nums) <= step:
            print(id(numbers))
            print(id(removing))
            my_list.append(int(nums))
            removing.remove(nums)
    print(f"Group of {step}'s: {my_list}")
    step += 10
    numbers = removing
    print("for loop ends")

print(id(numbers))
print(id(removing))