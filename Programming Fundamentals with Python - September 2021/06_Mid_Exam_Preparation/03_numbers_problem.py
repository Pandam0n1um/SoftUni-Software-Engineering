def Average(lst):
    return sum(lst) / len(lst)


value_list = [int(i) for i in input().split()]
value_list=sorted(value_list,reverse=True)
mean_value = Average(value_list)
filtered_list = [str(i) for i in value_list if i>mean_value]
print_list=filtered_list[:5:]
if len(print_list)>0:
    print(" ".join(print_list))
else:
    print("No")