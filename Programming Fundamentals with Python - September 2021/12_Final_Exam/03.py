def like():
    return


def dislike():
    return


disliked = 0
guests = {}
while True:
    command = input()
    if command == "Stop":
        break
    action, name, meal = command.split("-")
    if action == "Like":
        if not name in guests:
            guests[name] = {'liked': [],'disliked':[]}
        if not meal in guests[name]['liked'] and not meal in guests[name]['disliked']:
            guests[name]['liked'].append(meal)
    elif action == "Dislike":
        if not name in guests:
            print(f"{name} is not at the party.")
        elif not meal in guests[name]['liked']:
            print(f"{name} doesn't have the {meal} in his/her collection.")
        else:
            guests[name]['disliked'].append(meal)
            guests[name]['liked'].remove(meal)
            print(f"{name} doesn't like the {meal}.")
            disliked+=1
    # print(guests[name].values())

sorted_guests=sorted(guests.items(),key=lambda x: (-len(x[1]['liked']),x[0]))

for guest,meal in sorted_guests:
    print(f"{guest}: {', '.join(meal['liked'])}")
print(f"Unliked meals: {disliked}")