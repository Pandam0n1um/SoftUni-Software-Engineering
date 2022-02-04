divisor=int(input())
bound=int(input())
is_found=False
multiple=None
for N in range(0,bound+1):
    if (N%divisor)==0:
        is_found=True
        multiple=N

print(multiple)