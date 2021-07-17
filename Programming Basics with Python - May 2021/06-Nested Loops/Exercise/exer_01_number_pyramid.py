value=int(input())
limit_value=0

for row in range(1, value+1):
    for col in range(1, row+1):
        limit_value+=1
        print(f"{limit_value} ", end='')
        if  limit_value==value:
            break
    print()
    if limit_value==value:
        break