n_result=int(input())
combinations_counter=0
for n1 in range (n_result+1):
    for n2 in range (n_result+1):
        for n3 in range (n_result+1):
            if n1+n2+n3==n_result:
                combinations_counter+=1

print(combinations_counter)

