whiskey_price = float(input())

beer_amount = float(input())

wine_amount = float(input())

rakia_amount = float(input())

whiskey_amount = float(input())

rakia_price = whiskey_price * 0.5

wine_price = rakia_price * 0.6

beer_price = rakia_price * 0.2

whiskey_total_cost = float(whiskey_amount * whiskey_price)

rakia_total_cost = float(rakia_amount * rakia_price)

wine_total_cost = float(wine_amount * wine_price)

beer_total_cost = float(beer_amount * beer_price)

alc_total_cost = (whiskey_total_cost + rakia_total_cost + wine_total_cost + beer_total_cost)

print(f"{alc_total_cost:.2f}")
