from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary1: float, salary2: float, *children):
        count = 2 + len(children)
        super().__init__(family_name, salary1 + salary2, count)
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * count
        self.calculate_expenses(self.appliances,self.children)

