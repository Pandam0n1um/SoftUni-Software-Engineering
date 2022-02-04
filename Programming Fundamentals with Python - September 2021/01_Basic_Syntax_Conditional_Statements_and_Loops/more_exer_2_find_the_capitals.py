init_string = input()
capitals_list=[]
for index in range(0, len(init_string)):
    if 64<ord(init_string[index])<91:
        capitals_list.append(index)

print(capitals_list)