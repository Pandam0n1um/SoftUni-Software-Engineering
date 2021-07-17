budget = int(input())

season = str(input())

fishermen_count = int(input())

discounted_price_boat = None
nominal_price_boat = None

if season == str("Spring"):
    nominal_price_boat = 3000
elif season == str("Summer") or season == str("Autumn"):
    nominal_price_boat = 4200
elif season == str("Winter"):
    nominal_price_boat = 2600

if fishermen_count <= 6:
    discounted_price_boat = (nominal_price_boat * 0.9)
elif 7 <= fishermen_count <= 11:
    discounted_price_boat = (nominal_price_boat * 0.85)
elif 12 <= fishermen_count:
    discounted_price_boat = (nominal_price_boat * 0.75)

if fishermen_count % 2 == 0 and season != str('Autumn'):
    discounted_price_boat = (discounted_price_boat * 0.95)
else:
    pass

diff = abs(budget - discounted_price_boat)

if discounted_price_boat <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
