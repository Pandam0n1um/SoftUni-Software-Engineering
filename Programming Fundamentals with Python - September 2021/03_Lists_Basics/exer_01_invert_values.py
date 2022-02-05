input_string=input()

my_list=input_string.split(" ")

for i in range(len(my_list)):
    my_list[i]=-int(my_list[i])
print(my_list)