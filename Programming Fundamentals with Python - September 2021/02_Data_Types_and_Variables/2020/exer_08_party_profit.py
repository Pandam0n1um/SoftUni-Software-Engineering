party_size = int(input())

days_count = int(input())

coins = 0

for days in range(1, days_count + 1):
    if days%10==0:
        party_size-=2
    if days%15==0:
        party_size+=5
    coins += 50
    coins-=(party_size*2)
    if days % 3 == 0:
        coins -= (party_size * 3)

    if days % 5 == 0:
        coins += (party_size * 20)
    if days % 5 == 0 and days%3==0:
        coins-= (party_size * 2)


coins_per_person=coins//party_size

print(f"{party_size} companions received {coins_per_person} coins each.")