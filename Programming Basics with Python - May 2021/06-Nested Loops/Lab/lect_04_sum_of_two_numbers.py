interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
combination_counter = 0
is_magic = False
n1=0
n2=0

for n1 in range(interval_start, interval_end + 1):
    for n2 in range(interval_start, interval_end + 1):
        combination_counter += 1
        if n1 + n2 == magic_number:
            is_magic = True
            break
    if is_magic==True:
        break

if is_magic:
    print(f"Combination N:{combination_counter} ({n1} + {n2} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
