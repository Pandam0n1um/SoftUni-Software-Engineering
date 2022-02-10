n = int(input())
synonim_dict = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonim_dict:
        synonim_dict[word]=[]
    synonim_dict[word].append(synonym)

for key,value in synonim_dict.items():
    print(f"{key} - {', '.join(value)}")