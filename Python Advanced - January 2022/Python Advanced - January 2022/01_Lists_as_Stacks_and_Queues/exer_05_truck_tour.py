count_pumps = int(input())

point = -1

total_gas=0
total_distance=0

for i in range(count_pumps):
    petrol, distance = [int(el) for el in input().split()]
    total_gas += petrol
    total_distance += distance
    if total_gas < total_distance:
        point=-1
        total_gas=0
        total_distance=0
    else:
        if point<0:
            point = i
if point>=0:
    print(point)
