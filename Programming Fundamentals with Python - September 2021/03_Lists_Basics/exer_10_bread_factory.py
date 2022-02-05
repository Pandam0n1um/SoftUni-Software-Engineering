energy = 100
coins = 100

working_day_events = input().split("|")
is_completed = False

for days in range(len(working_day_events)):
    current_day = working_day_events[days].split("-")
    current_day_event = current_day[0]
    value = int(current_day[1])
    if current_day_event == "rest":
        increment = 0
        if energy < 100:
            difference = 100 - energy
            increment = min(difference, value)
            energy += increment

        print(f"You gained {increment} energy.")
        print(f"Current energy: {energy}.")

    elif current_day_event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - value <= 0:
            print(f"Closed! Cannot afford {current_day_event}.")
            break
        else:
            coins -= value
            print(f"You bought {current_day_event}.")
    if days + 1 == len(working_day_events):
        is_completed = True

if is_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
