count=int(input())

even=set()
odd=set()

for line in range(1,count+1):
    value=sum([ord(el) for el in input()])//line
    if value%2==0:
        even.add(value)
    else:
        odd.add(value)
if sum(even)==sum(odd):
    print(*odd.union(even),sep=",")
elif sum(odd)>sum(even):
    print(*odd.difference(even),sep=",")
else:
    print(*odd.symmetric_difference(even),sep=", ")