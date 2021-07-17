stadium_capacity = int(input())
fans_amount = int(input())
counter_sector_a = 0
counter_sector_b = 0
counter_sector_v = 0
counter_sector_g = 0

for fans in range(fans_amount):
    stadium_sector = str(input())
    if stadium_sector == "A":
        counter_sector_a += 1
    elif stadium_sector == "B":
        counter_sector_b += 1
    elif stadium_sector == "V":
        counter_sector_v += 1
    elif stadium_sector == "G":
        counter_sector_g += 1


print(f"{(counter_sector_a*100/fans_amount):.2f}%")
print(f"{(counter_sector_b*100/fans_amount):.2f}%")
print(f"{(counter_sector_v*100/fans_amount):.2f}%")
print(f"{(counter_sector_g*100/fans_amount):.2f}%")
print(f"{(fans_amount*100/stadium_capacity):.2f}%")