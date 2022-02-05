
# def palindrome_integers_check(integer_string):
#     integer_list = integer_string.split(", ")
#     integer_list_bool = []
#
#     for index in range(len(integer_list)):
#         current_number = integer_list[index]
#
#         mid_string = 0
#         is_palindrome = None
#         if len(current_number) == 1:
#             is_palindrome = True
#         elif len(current_number) % 2 == 0:
#             mid_string = len(current_number) // 2
#         else:
#             mid_string = len(current_number) // 2
#
#         for pos in range(mid_string):
#             if current_number[pos] == current_number[-(1 + pos)]:
#                 is_palindrome = True
#             else:
#                 is_palindrome = False
#         integer_list_bool.append(is_palindrome)
#
#     return integer_list_bool
#
#
# int_list = input()
#
# result = (palindrome_integers_check(int_list))
#
# for index in range(len(result)):
#     print(result[index])
