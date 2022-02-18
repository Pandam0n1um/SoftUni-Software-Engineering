nums=tuple([float(el) for el in input().split()])

count={}

for num in nums:
    if not num in count:
        count[num]=0
    count[num]+=1

for num,amount in count.items():
    print(f"{num} - {amount} times")

