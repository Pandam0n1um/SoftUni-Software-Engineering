# integer_list_string = input()
# integer_list = [int(x) for x in integer_list_string.split()]
# removed_count = int(input())
#
# for _ in range(removed_count):
#     integer_list.remove(min(integer_list))
#
# print(*integer_list, sep=", ")


integer_list = [int(i) for i in input().split()]
removed_count = int(input())

for _ in range(removed_count):
    integer_list.remove(min(integer_list))

print(*integer_list, sep=", ")