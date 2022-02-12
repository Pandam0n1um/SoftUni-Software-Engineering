list_split=input()
for i in range(len(list_split)):
    if list_split[i]==":" :
        print(f":{list_split[i+1]}")
        i+=1
#
#         # and i < (len(list_split))


given_string = input()
list_of_emos = []
while given_string:
    emo = ""
    emo_start = given_string.find(":")
    emo += given_string[emo_start: emo_start + 2]
    list_of_emos.append(emo)
    given_string = given_string[emo_start+2:]
print(*list_of_emos, sep="\n")