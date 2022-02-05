sent_off_a = []
sent_off_b = []
sent_off_string = input()
sent_off_list = sent_off_string.split(" ")

for i in range(len(sent_off_list)):
    if "A" in sent_off_list[i]:
        if sent_off_list[i] in sent_off_a:
            continue
        sent_off_a.append(sent_off_list[i])
    elif "B" in sent_off_list[i]:
        if sent_off_list[i] in sent_off_b:
            continue
        sent_off_b.append(sent_off_list[i])
    if len(sent_off_a) > 4 or len(sent_off_b) > 4:
        break

team_a = 11 - len(sent_off_a)
team_b = 11 - len(sent_off_b)

print(f"Team A - {team_a}; Team B - {team_b}")

if team_a < 7 or team_b < 7:
    print("Game was terminated")
