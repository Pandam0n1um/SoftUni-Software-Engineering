chrisantemum_count = int(input())
rose_count = int(input())
tulip_count = int(input())
season = str(input())
holiday_check = str(input())

total_flowers_count = (chrisantemum_count + rose_count + tulip_count)

chrisantemum_cost = None
rose_cost = None
tulip_cost = None

if season == str("Spring") or season == str("Summer"):
    chrisantemum_cost = 2.00
    rose_cost = 4.10
    tulip_cost = 2.50

    if holiday_check == str("Y"):
        chrisantemum_cost = (chrisantemum_cost * 1.15)
        rose_cost = (rose_cost * 1.15)
        tulip_cost = (tulip_cost * 1.15)
    else:
        pass

elif season == str("Autumn") or season == str("Winter"):
    chrisantemum_cost = 3.75
    rose_cost = 4.50
    tulip_cost = 4.15

    if holiday_check == str("Y"):
        chrisantemum_cost = (chrisantemum_cost * 1.15)
        rose_cost = (rose_cost * 1.15)
        tulip_cost = (tulip_cost * 1.15)
    else:
        pass

total_nominal_cost = (chrisantemum_count * chrisantemum_cost + rose_count * rose_cost + tulip_count * tulip_cost)

total_discounted_cost = total_nominal_cost

if 7 <= tulip_count and season == str("Spring"):
    total_discounted_cost = (total_nominal_cost * 0.95)

elif 10 <= rose_count and season == str("Winter"):
    total_discounted_cost = (total_nominal_cost * 0.90)


if 20 < total_flowers_count:
    total_discounted_cost = (total_discounted_cost * 0.8)

total_cost = (total_discounted_cost + 2)

print(f"{total_cost:.2f}")
