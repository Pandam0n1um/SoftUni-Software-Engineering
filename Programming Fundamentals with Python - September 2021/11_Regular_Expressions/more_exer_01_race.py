import re

participants={value: {'distance':0} for value in input().split(", ")}
pattern_name=r"[a-zA-Z]"
pattern_distance=r"[0-9]"
while True:
    command=input()
    if command=="end of race":
        break
    curr_name="".join(re.findall(pattern_name,command))
    if curr_name in participants:
        curr_distance=sum([int(x) for x in re.findall(pattern_distance,command)])
        participants[curr_name]['distance']+=curr_distance

sorted_part=sorted(participants.items(),key=lambda x: -x[1]['distance'])


print(f"1st place: {sorted_part[0][0]}")
print(f"2nd place: {sorted_part[1][0]}")
print(f"3rd place: {sorted_part[2][0]}")

# print(sorted_part)