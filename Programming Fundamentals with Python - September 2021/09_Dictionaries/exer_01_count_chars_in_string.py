inp_string=input()
dict_chars={}
for char in inp_string:
    if char==" ":
        pass
    elif char not in dict_chars:
        dict_chars[char]=1
    else:
        dict_chars[char]+=1

result=""

for key,val in dict_chars.items():
    print(f"{key} -> {val}")

