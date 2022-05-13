from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    INITIAL_SIZE = 200

    def __init__(self, name, price):
        super().__init__(name, Bread.INITIAL_SIZE, price)
