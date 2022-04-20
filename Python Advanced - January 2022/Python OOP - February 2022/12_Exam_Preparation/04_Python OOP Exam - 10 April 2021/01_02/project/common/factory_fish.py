from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class FactoryFish:
    valid_fish = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish,
    }

    def create_fish(self, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type in self.valid_fish:
            return self.valid_fish[fish_type](fish_name, fish_species, price)
        return None
