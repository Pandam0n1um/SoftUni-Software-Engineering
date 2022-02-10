list_censored=input().split(", ")
text=input()

for word in list_censored:
    while word in text:
        text=text.replace(word,"*"*len(word))

print(text)