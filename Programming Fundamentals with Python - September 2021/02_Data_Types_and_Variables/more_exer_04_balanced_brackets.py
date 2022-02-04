number_lines = int(input())
is_balanced = True
is_open = False
is_false = False
is_double_opened = False
last_string = ""

for i in range(number_lines):
    string_input = input()
    if not is_open and string_input == ")":
        is_false = True
    if string_input == "(":
        is_open = True
        is_balanced = False
    if is_open and last_string == "(" and last_string == string_input:
        is_balanced = False
        is_double_opened = True
    if is_open and string_input == ")":
        is_open = False
        is_balanced = True
    last_string = string_input

if not is_open and is_balanced and not is_false and not is_double_opened:
    print("BALANCED")
else:
    print("UNBALANCED")
