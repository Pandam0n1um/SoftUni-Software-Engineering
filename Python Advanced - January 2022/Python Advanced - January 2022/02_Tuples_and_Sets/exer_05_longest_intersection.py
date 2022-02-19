def input_line(value):
    longest_intersection={}
    for _ in range(value):
        first,second=input().split("-")
        first_start,first_end=first.split(",")
        second_start,second_end=second.split(",")
        first_set={el for el in range(int(first_start),int(first_end)+1)}
        second_set={el for el in range(int(second_start),int(second_end)+1)}
        curr=intersection(first_set,second_set)
        if len(curr)>len(longest_intersection):
            longest_intersection=curr
    return longest_intersection


def intersection(set_one, set_two):
    return set_one.intersection(set_two)


count= int(input())

longest = [str(el) for el in input_line(count)]

print(f"Longest intersection is [{', '.join(longest)}] with length {len(longest)}")