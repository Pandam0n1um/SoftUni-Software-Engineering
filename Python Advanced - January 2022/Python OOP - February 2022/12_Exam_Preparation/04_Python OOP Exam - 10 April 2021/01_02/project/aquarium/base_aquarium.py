from abc import ABC, abstractmethod

from project.common.validators import Validator
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    POSSIBLE_FISH_TYPES = (
        'FreshwaterFish',
        'SaltwaterFish',
    )

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

        self.decorations = []
        self.fish = []

    @property
    @abstractmethod
    def fish_type(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Aquarium name cannot be an empty string."
        Validator.validate_string_empty(value, error_message)
        self.__name = value

    def calculate_comfort(self):
        comfort = 0
        for decoration in self.decorations:
            comfort += decoration.comfort
        return comfort

    def add_fish(self, fish: BaseFish):
        if len(self.fish) == self.capacity:
            return f"Not enough capacity."
        if not self.fish_type == fish.__class__.__name__:
            return "Water not suitable."
        if fish.__class__.__name__ in self.__class__.POSSIBLE_FISH_TYPES:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_status = 'none' if len(self.fish) == 0 else ' '.join([fish.name for fish in self.fish])
        return f"{self.name}:\n" + \
               f"Fish: {fish_status}\n" + \
               f"Decorations: {len(self.decorations)}\n" + \
               f"Comfort: {self.calculate_comfort()}"
