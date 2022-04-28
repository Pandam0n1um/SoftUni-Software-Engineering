from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREMENT_EAT = 2
    INITIAL_SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)
