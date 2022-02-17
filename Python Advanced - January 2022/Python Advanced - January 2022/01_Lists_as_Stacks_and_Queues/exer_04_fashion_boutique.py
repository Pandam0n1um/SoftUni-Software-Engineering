from collections import deque

box=deque([int(el) for el in input().split()])
rack_cap=int(input())

rack_count=1
current_rack=0
while box:
    current=box.pop()
    if (current_rack+current)<=rack_cap:
        current_rack+=current
    else:
        current_rack=current
        rack_count+=1

print(rack_count)