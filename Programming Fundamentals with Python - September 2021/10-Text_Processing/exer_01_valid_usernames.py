usernames = input().split(", ")

for name in usernames:
    is_valid = 0
    is_length = False
    if 3 <= len(name) <= 16:
        is_length = True

    for char in name:
        if char.isalnum() or ord(char) == 95 or ord(char) == 45:
            is_valid += 1
        else:
            is_valid = 0
            break
    if is_valid > 1 and is_length:
        print(name)
