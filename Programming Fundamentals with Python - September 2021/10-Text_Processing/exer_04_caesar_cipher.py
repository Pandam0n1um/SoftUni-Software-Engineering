init_string=input()
result=""
for sym in init_string:
    result+=chr(ord(sym)+3)

print(result)