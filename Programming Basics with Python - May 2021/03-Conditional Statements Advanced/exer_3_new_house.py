flowers_type = str(input())

flowers_count = int(input())

budget = int(input())


flower_unit_price = None

if flowers_type == str('Roses'):
    rose_price = 5
    if flowers_count <= 80:
        flower_unit_price = rose_price
    else:
        flower_unit_price = (rose_price * 0.9)

elif flowers_type == str('Dahlias'):
    dahlia_price = 3.80
    if flowers_count <= 90:
        flower_unit_price = dahlia_price
    else:
        flower_unit_price = (dahlia_price * 0.85)

elif flowers_type == str('Tulips'):
    tulip_price = 2.80
    if flowers_count <= 80:
        flower_unit_price = tulip_price
    else:
        flower_unit_price = (tulip_price * 0.85)

elif flowers_type == str('Narcissus'):
    narcissus_price = 3
    if flowers_count < 120:
        flower_unit_price = (narcissus_price * 1.15)
    else:
        flower_unit_price = narcissus_price

elif flowers_type == str('Gladiolus'):
    gladiolus_price = 2.50
    if flowers_count < 80:
        flower_unit_price = (gladiolus_price * 1.20)
    else:
        flower_unit_price = gladiolus_price

total_cost = (flower_unit_price * flowers_count)

diff = abs(budget - total_cost)

if total_cost <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
