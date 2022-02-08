adv_days = int(input())
players_count = int(input())
group_energy = float(input())
water_daily = float(input())
food_daily = float(input())
is_nrg_enough = True

total_water = water_daily * adv_days * players_count
total_food = food_daily * adv_days * players_count

for day in range(1, adv_days+1):
    energy_loss = float(input())
    group_energy -= energy_loss

    if group_energy <= 0:
        is_nrg_enough = False
        break

    if day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.7
    if day % 3 == 0:
        group_energy *= 1.1
        total_food -= (total_food / players_count)

if is_nrg_enough:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
