moves_amount = int(input())
total_points = 0

counter_0_9 = 0
counter_10_19 = 0
counter_20_29 = 0
counter_30_39 = 0
counter_40_50 = 0
counter_invalid=0
for move in range(moves_amount):
    new_points = int(input())
    if 0 <= new_points <= 9:
        counter_0_9 += 1
        total_points += (new_points * 0.2)
    elif 10 <= new_points <= 19:
        counter_10_19 += 1
        total_points += (new_points * 0.3)
    elif 20 <= new_points <= 29:
        counter_20_29 += 1
        total_points += (new_points * 0.4)
    elif 30 <= new_points <= 39:
        counter_30_39 += 1
        total_points += 50
    elif 40 <= new_points <= 50:
        counter_40_50 += 1
        total_points += 100
    elif new_points < 0 or 50 < new_points:
        counter_invalid+=1
        total_points*=0.5

print(f"{total_points:.2f}")
print(f"From 0 to 9: {(counter_0_9/moves_amount)*100:.2f}%")
print(f"From 10 to 19: {(counter_10_19/moves_amount)*100:.2f}%")
print(f"From 20 to 29: {(counter_20_29/moves_amount)*100:.2f}%")
print(f"From 30 to 39: {(counter_30_39/moves_amount)*100:.2f}%")
print(f"From 40 to 50: {(counter_40_50/moves_amount)*100:.2f}%")
print(f"Invalid numbers: {(counter_invalid/moves_amount)*100:.2f}%")