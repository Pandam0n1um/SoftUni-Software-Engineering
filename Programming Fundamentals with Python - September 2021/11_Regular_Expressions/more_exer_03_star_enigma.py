import re
count_lines=int(input())
planet_status={'Attacked':[],'Destroyed':[]}
for i in range(count_lines):
    text = input()
    pattern = r"[star]"
    reductor = len(re.findall(pattern, text, re.IGNORECASE))

    pattern_split = r"(?<=\@)(?P<pl_name>[a-zA-Z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*!(?P<attack>[AD])![^@!:>-]*->((?P<soldiers>\d+))"

    decoded_message="".join([chr(ord(x)-reductor) for x in text])
    curr_dict=re.search(pattern_split,decoded_message)
    if curr_dict:
        curr_dict=curr_dict.groupdict()
        if curr_dict['attack']=="A":
            planet_status['Attacked'].append(curr_dict['pl_name'])
        elif curr_dict['attack']=="D":
            planet_status['Destroyed'].append(curr_dict['pl_name'])

for attack,pl_list in planet_status.items():
    print(f"{attack} planets: {len(pl_list)}",end="")
    pl_list_sorted=sorted(pl_list)
    planet_print="".join([f"\n-> {x}" for x in pl_list_sorted])
    print(planet_print)

