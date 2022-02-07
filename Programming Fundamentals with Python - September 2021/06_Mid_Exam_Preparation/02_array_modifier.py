value_list = [int(i) for i in input().split()]

while True:
    command = input().split()
    index1 = 0
    index2 = 0
    action = command[0]
    if action == "end":
        break

    if action == "swap" or action == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])

    if action == "swap":
        value_list[index1], value_list[index2] = value_list[index2], value_list[index1]
    elif action == "multiply":
        value_list[index1]=value_list[index1]*value_list[index2]
    elif action == "decrease":
        value_list=[i-1 for i in value_list]
value_list=[str(i) for i in value_list]
print(", ".join(value_list))