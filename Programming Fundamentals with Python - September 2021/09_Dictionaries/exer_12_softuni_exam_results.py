dict_languages={}
dict_points={'banned':[]}

while True:
    command=input().split("-")
    if command[0]=="exam finished":
        break

    username=command[0]
    language=command[1]
    if language=="banned":
        dict_points['banned'].extend(dict_points[username])
        del(dict_points[username])
        continue
    points=int(command[2])
    if username not in dict_points:
        dict_points[username]=[]
    if language not in dict_languages:
        dict_languages[language]=[]
    dict_languages[language].append(username)
    dict_points[username].append(points)

del dict_points['banned']
dict_points_sorted=dict(sorted(dict_points.items(),key= lambda kvp: (-max(kvp[1]),kvp[0])))
dict_languages_sorted=dict(sorted(dict_languages.items(),key=lambda kvp:(-len(kvp[1]),kvp[0])))

print("Results:")

for user,value in dict_points_sorted.items():
    print(f"{user} | {max(value)}")
print("Submissions:")
for language,count in dict_languages_sorted.items():
    print(f"{language} - {len(count)}")

# print(dict_languages.items())
# print(dict_points.items())
# print(dict_languages.items())
# print(dict_points_sorted.items())
