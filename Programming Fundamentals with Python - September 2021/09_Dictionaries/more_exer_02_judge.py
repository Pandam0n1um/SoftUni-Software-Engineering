dict_contests={}
dict_results={}

while True:
    is_present=False
    command=input()
    if command=="no more time":
        break
    username,contest,points=command.split(" -> ")
    points=int(points)
    if contest not in dict_contests:
        dict_contests[contest]={}
    if username in dict_contests[contest]:
        curr_value=dict_contests[contest][username]
        dict_contests[contest][username]=max(curr_value,points)
    else:
        dict_contests[contest][username]=points


for contest,result in dict_contests.items():
    for username, points in result.items():
        if username not in dict_results:
            dict_results[username] = (points)
        else:
            dict_results[username]+=((points))

    print(f"{contest}: {len(result)} participants")
    sorted_part=sorted(result.items(),key=lambda x: (-x[1],x[0]))
    pos = 1
    for i in sorted_part:
        name,points=i
        print(f"{pos}. {name} <::> {points} ")
        pos+=1

dict_results_sorted=sorted(dict_results.items(),key=lambda x: (-x[1],x[0]))

pos = 1
print("Individual standings:")
for i in dict_results_sorted:
    name, points = i
    print(f"{pos}. {name} -> {points} ")
    pos+=1

# print("")
# print(dict_results_sorted)

