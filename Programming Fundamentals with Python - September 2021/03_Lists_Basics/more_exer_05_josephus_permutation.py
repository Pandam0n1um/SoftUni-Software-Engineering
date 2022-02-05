# circle = input().split(" ")
# k_value = int(input()) - 1
#
# result = []
# index = 0
#
# while not len(circle) == 0:
#     index += k_value
#
#     if index >= len(circle):
#         index = (index % len(circle))
#
#     killed = circle.pop(index)
#     result.append(int(killed))
#
# print(str(result).replace(" ", ""))

# if len(input_list)==1:
#     index=0
# el

# alive = input().split(" ")
# step = int(input())
# executed = []
# index = 0
# while True:
#     index = (index + step - 1) % len(alive)
#     executed.append(alive[index])
#     alive.remove(alive[index])
#     if len(alive) == 0:
#         break
# executed=[int(x) for x in executed]
# print(str(executed).replace(" ", ""))