number_lines = int(input())
carplates = {}

for lines in range(number_lines):
    command = input().split()
    action = command[0]
    user = command[1]

    if action == "register":
        plate_number = command[2]
        if user not in carplates:
            carplates[user] = plate_number
            print(f"{user} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {carplates[user]}")

    else:
        if user not in carplates:
            print(f"ERROR: user {user} not found")
        else:
            carplates.pop(user)
            print(f"{user} unregistered successfully")

for user, plate in carplates.items():
    print(f"{user} => {plate}")
