list_str=input().split()
result=""
for word in list_str:
    result+=word*len(word)
print(result)