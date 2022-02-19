def input_line(value):
    chem_elem=set()
    for _ in range(value):
        [chem_elem.add(el) for el in input().split()]
    return chem_elem

# unique_chem_elem=set('George George George Peter George NiceGuy1234'.split())

count=int(input())
unique_chem_elem=input_line(count)

print(*unique_chem_elem,sep='\n')