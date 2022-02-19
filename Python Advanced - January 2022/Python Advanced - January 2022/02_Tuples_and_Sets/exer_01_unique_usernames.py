def input_line(value):
    names=set()
    for _ in range(value):
        names.add(input())
    return names

# unique_names=set('George George George Peter George NiceGuy1234'.split())

count=int(input())
unique_names=input_line(count)

print(*unique_names,sep='\n')