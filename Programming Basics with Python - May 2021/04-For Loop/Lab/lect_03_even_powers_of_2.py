import math

power_of_2 = int(input())

for i in range(0, power_of_2 + 1, 2):
    value = int(math.pow(2, i))
    print(value)
