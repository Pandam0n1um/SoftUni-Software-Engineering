from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea


bakery=Bakery('Wiener')
skalichka=Cake('Skalichka',3.20)
print(skalichka)
# print(bakery.add_food('Cake','Skalichka',3.20))
# print(bakery.add_food('Cake','Skalichka',4.20))
print(bakery.add_food('Bread','Fullgrain',0))
print(bakery.add_food('Bread','Fullgrain',4.20))


# roiboos=Tea('Roiboos',250,'Lechitel')
#
# print(roiboos)