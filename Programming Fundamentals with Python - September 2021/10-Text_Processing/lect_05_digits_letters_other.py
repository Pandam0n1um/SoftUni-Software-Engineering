line_str=input()
sym_dig=""
sym_let=""
sym_oth=""

for character in line_str:
    if character.isalpha():
        sym_let+=character
    elif character.isnumeric():
        sym_dig+=character
    else:
        sym_oth+=character

print(sym_dig)
print(sym_let)
print(sym_oth)