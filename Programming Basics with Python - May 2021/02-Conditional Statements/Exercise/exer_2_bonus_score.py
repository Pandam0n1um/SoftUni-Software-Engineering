init_score = int(input())
bonus = 0

if init_score <= 100:
    bonus = 5

elif 100 < init_score < 1000:
    bonus = init_score * 0.2

elif init_score > 1000:
    bonus = init_score * 0.1

if init_score % 2 == 0:
    bonus = bonus + 1

elif init_score % 10 == 5:
    bonus = bonus + 2

print(bonus)

print(bonus+init_score)
