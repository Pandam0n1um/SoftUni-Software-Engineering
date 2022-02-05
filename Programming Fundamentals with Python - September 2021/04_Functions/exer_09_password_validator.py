def is_password_valid(password_str):
    is_length = False
    is_alphanum = password_str.isalnum()
    is_digit_count = False
    digit = 0
    if 6 <= len(password_str) <= 10:
        is_length = True
    for pos in password_str:
        if pos.isnumeric():
            digit += 1
    if digit >= 2:
        is_digit_count = True
    return is_length, is_alphanum, is_digit_count


password = input()

result = is_password_valid(password)

if not result[0]:
    print("Password must be between 6 and 10 characters")
if not result[1]:
    print("Password must consist only of letters and digits")
if not result[2]:
    print("Password must have at least 2 digits")
if result[0] and result[1] and result[2]:
    print("Password is valid")
