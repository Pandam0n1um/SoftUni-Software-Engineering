command = input()
coffee_counter = 0

while not command == "END":
    is_lower = False
    is_valid = False
    is_sleep_needed = False
    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        is_valid = True

    if command.islower():
        is_lower = True

    if is_valid and is_lower:
        coffee_counter += 1
    if is_valid and (not is_lower):
        coffee_counter += 2

    if coffee_counter > 5:
        is_sleep_needed = True
        break
    command=input()

if not is_sleep_needed:
    print(f"{coffee_counter}")
else:
    print("You need extra sleep")