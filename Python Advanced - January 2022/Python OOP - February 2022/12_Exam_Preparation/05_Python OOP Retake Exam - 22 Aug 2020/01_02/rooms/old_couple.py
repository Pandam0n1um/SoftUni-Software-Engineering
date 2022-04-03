from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension1: float,pension2: float):
        super().__init__(family_name, pension1+pension2,2)
        self.room_cost = 15
        self.appliances=[TV(),Fridge(),Stove()]*2
        self.calculate_expenses(self.appliances)

