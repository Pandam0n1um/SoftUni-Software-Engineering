from project.drink.drink import Drink


class Water(Drink):
    TEA_PRICE = 1.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, Water.TEA_PRICE, brand)
