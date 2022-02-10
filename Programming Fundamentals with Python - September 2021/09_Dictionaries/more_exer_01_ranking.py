contest_storage = {}
result_storage = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contest_storage[contest] = password

contestant_storage = {}

while True:
    command = input()
    if command == "end of submissions":
        break
    contest_inp, password_inp, username_inp, points_inp = command.split("=>")
    if contest_storage.get(contest_inp) == password_inp:
        if contest_inp not in contestant_storage:
            contestant_storage[contest_inp] = {}
        if username_inp in contestant_storage[contest_inp]:
            curr_value = contestant_storage[contest_inp][username_inp]
            contestant_storage[contest_inp][username_inp] = max(curr_value, int(points_inp))
        else:
            contestant_storage[contest_inp][username_inp] = int(points_inp)

for contest, user in contestant_storage.items():
    for username, points in user.items():
        if username not in result_storage:
            result_storage[username] = []
        result_storage[username].append({contest: int(points)})
result_storage_sorted = dict(sorted(result_storage.items(), key=lambda x: x[0]))

# print(result_storage_sorted)
max_points = 0
top_student = ""
for user, contests in result_storage_sorted.items():
    res = sum([sum(list(sub.values())) for sub in contests])
    if res > max_points:
        max_points = res
        top_student = user

print(f"Best candidate is {top_student} with total {max_points} points.")
print("Ranking:")
for user, contest in result_storage_sorted.items():
    print(user)
    contest.sort(key=lambda x: list(x.values()), reverse=True)
    for competition in contest:
        for k,v in competition.items():
            print(f"#  {k} -> {v}")