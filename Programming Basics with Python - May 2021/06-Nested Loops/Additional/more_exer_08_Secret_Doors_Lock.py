hundreds_upper_limit=int(input())
tenths_upper_limit=int(input())
units_upper_limit=int(input())

for hundreds in range (1,hundreds_upper_limit+1):
    if hundreds%2==1:
        continue
    if tenths_upper_limit>7:
        tenths_upper_limit=7
    for tenths in range(2, tenths_upper_limit + 1):
        counter_dividers = 0
        for i in range(1, tenths + 1):
            if tenths % i == 0:
                counter_dividers += 1
        if not(counter_dividers == 2):
            continue
        for units in range(1, units_upper_limit + 1):
            if units % 2 == 1:
                continue
            print(f"{hundreds} {tenths} {units}")
