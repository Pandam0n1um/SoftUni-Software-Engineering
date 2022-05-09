from project.drink.drink import Drink


class Tea(Drink):
    TEA_PRICE = 2.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion,Tea.TEA_PRICE, brand)

