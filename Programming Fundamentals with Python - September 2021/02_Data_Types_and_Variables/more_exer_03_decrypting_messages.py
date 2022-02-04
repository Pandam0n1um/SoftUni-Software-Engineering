key_value=int(input())
number_lines=int(input())
result=""
for i in range(number_lines):
    ord_input=ord(input())
    result+=chr(ord_input+key_value)

print(result)