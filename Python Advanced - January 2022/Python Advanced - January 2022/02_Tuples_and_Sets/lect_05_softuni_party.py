count = int(input())

vip = set()
regular = set()


for _ in range(count):
    reservation=input()
    if reservation[0].isnumeric():
        vip.add(reservation)
    else:
        regular.add(reservation)
while True:
    command=input()
    if command=="END":
        break
    if command in vip:
        vip.discard(command)
    elif command in regular:
        regular.discard(command)

vip=sorted(vip)
regular=sorted(regular)
missing=vip+regular
print(len(missing))
if missing:
    [print(el) for el in missing]
