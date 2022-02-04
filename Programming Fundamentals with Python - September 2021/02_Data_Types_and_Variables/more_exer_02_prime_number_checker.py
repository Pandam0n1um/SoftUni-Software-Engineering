import time


start = time.time()

# init_number = int(input())
#
# divider_counter = 0
#
# for i in range(2, init_number):
#     if init_number % i == 0:
#         divider_counter += 1
#
# if divider_counter == 0:
#     print("True")
# else:
#     print("False")
#
# init_number = int(input())
#
# end_range = init_number // 2 + 1
# for i in range(2, end_range):
#     if init_number % i == 0:
#         print("False")
#         break
#     else:
#         print("True")


number = int(input())
end_range = number // 2 + 1
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("False")
            break
    else:
        print("True")


end = time.time()
print("The time of execution of above program is :", end-start)