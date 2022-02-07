food_qty = float(input())*1000
hay_qty = float(input())*1000
cover_qty = float(input())*1000
guinea_weight = float(input())*1000
is_enough=True

days=30

for day in range(1,days+1):
    food_qty-=300
    if day%2==0:
        hay_qty-=(food_qty*0.05)
    if day%3==0:
        cover_qty-=(guinea_weight/3)

    if food_qty <= 0 or hay_qty <= 0 or cover_qty<=0:
        is_enough=False

if not is_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_qty/1000:.2f}, Hay: {hay_qty/1000:.2f}, Cover: {cover_qty/1000:.2f}.")