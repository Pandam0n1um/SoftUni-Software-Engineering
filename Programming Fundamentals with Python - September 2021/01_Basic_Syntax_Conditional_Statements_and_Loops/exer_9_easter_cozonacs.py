budget = float(input())
price_flour = float(input())

price_pack_eggs = 0.75 * price_flour
price_liter_milk = 1.25 * price_flour

cozonac_cost = (price_flour + price_pack_eggs + 0.25 * price_liter_milk)
cozonac_counter = 0
coloured_eggs_counter = 0

while True:
    if budget < cozonac_cost:
        break
    cozonac_counter += 1
    coloured_eggs_counter += 3
    budget -= cozonac_cost
    if cozonac_counter % 3 == 0:
        coloured_eggs_counter -= (cozonac_counter - 2)

print(f"You made {cozonac_counter} loaves of Easter bread! Now you have {coloured_eggs_counter} eggs and {budget:.2f}BGN left.")

# budget=float(input())
#
# price_flour=float(input())
#
# price_pack_eggs=0.75*price_flour
#
# price_liter_milk=1.25*price_flour
# milk=0
#
# cozonac_counter=0
# coloured_eggs_counter=0
#
# while True:
#     if (budget<(price_flour+price_pack_eggs) and not milk==0) or (budget<(price_flour+price_pack_eggs+price_liter_milk and milk==0)):
#         break
#     if not milk>0:
#         budget-=price_liter_milk
#         milk=1
#     else:
#         milk-=0.25
#     cozonac_counter+=1
#     coloured_eggs_counter+=3
#     budget-=(price_pack_eggs+price_flour)
#     if cozonac_counter%3==0:
#         coloured_eggs_counter-=(cozonac_counter-2)
#
# print(f"You made {cozonac_counter} cozonacs! Now you have {coloured_eggs_counter} eggs and {budget}BGN left.")


budget = float(input())

price_flour = float(input())

price_pack_eggs = 0.75 * price_flour

price_liter_milk = 1.25 * price_flour

cozonac_cost = (price_flour + price_pack_eggs + 0.25 * price_liter_milk)
cozonac_counter = 0
coloured_eggs_counter = 0

while True:
    if budget < cozonac_cost:
        break
    cozonac_counter += 1
    coloured_eggs_counter += 3
    budget -= cozonac_cost
    if cozonac_counter % 3 == 0:
        coloured_eggs_counter -= (cozonac_counter - 2)

print(
    f"You made {cozonac_counter} loaves of Easter bread! Now you have {coloured_eggs_counter} eggs and {budget:.2f}BGN left.")
