health = 100
bitcoins = 0

rooms = input().split("|")
is_alive=True

room_counter = 0

for room in rooms:
    room_counter += 1
    command,value=room.split()
    value=int(value)
    if command == "potion":
        limit = 100 - health
        if value > limit:
            value = limit
        health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        monster = command
        health -= value
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_counter}")
            is_alive=False
            break

if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")