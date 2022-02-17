import re

password = input()

while True:
    command = input()
    if command == "Complete":
        break
    action, *tokens = command.split()

    if action == "Make":
        case = tokens[0]
        index = int(tokens[1])
        if not 0 <= index < len(password):
            continue
        if case == "Upper":
            changed = password[index].upper()
        else:
            changed = password[index].lower()
        password = password[:index] + changed + password[index + 1:]
    elif action == "Insert":
        char = tokens[1]
        index = int(tokens[0])
        if not 0 <= index < len(password):
            continue
        password = password[:index] + char + password[index:]
    elif action == "Replace":
        char = tokens[0]
        value = int(tokens[1])
        if not char in password:
            continue
        new_value = ord(char) + value
        password = password.replace(char, chr(new_value))
    elif action == "Validation":
        if len(password)<8:
            print("Password must be at least 8 characters long!")
        if not re.match(r'^[A-Za-z0-9_]+$', password):
            print("Password must consist only of letters, digits and _!")
        if not re.findall(r'[A-Z]+?', password):
            print("Password must consist at least one uppercase letter!")
        if not re.findall(r'[a-z]+?', password):
            print("Password must consist at least one lowercase letter!")
        if not re.findall(r'[0-9]+?', password):
            print("Password must consist at least one digit!")
        continue
    else:
        continue
    print(password)

