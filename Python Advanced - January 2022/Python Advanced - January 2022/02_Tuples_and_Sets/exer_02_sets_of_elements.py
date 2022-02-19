def input_line(value):
    nums = set()
    for _ in range(value):
        nums.add(input())
    return nums


def intersection(set_one, set_two):
    return set_one.intersection(set_two)


# first_set=set('1 3 5 7'.split())
# second_set=set('3 4 5'.split())

count_first,count_second = (int(el) for el in input().split())
# count_second = int(input())

first_set = input_line(count_first)
second_set = input_line(count_second)

print(*intersection(first_set,second_set),sep='\n')