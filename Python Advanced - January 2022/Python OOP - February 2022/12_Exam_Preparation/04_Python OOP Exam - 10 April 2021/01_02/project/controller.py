from project.common.factory_aquarium import FactoryAquarium
from project.common.factory_decorations import FactoryDecoration
from project.common.factory_fish import FactoryFish
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

        self.factory_aquarium = FactoryAquarium()
        self.factory_decoration = FactoryDecoration()
        self.factory_fish = FactoryFish()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        # aquarium = self.factory_aquarium.create_aquarium(aquarium_type, aquarium_name)
        # if aquarium:
        #     self.aquariums.append(aquarium)
        #     return f"Successfully added {aquarium_type}."
        # return "Invalid aquarium type."
        try:
            aquarium = self.factory_aquarium.create_aquarium(aquarium_type, aquarium_name)
            self.aquariums.append(aquarium)
            return f'Successfully added {aquarium_type}.'
        except ValueError as error:
            return str(error)

    def add_decoration(self, decoration_type: str):
        decoration = self.factory_decoration.create_decoration(decoration_type)
        if decoration:
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.add_decoration(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = self.factory_fish.create_fish(fish_type, fish_name, fish_species, price)
        if not fish:
            return f"There isn't a fish of type {fish_type}."
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                result = aquarium.add_fish(fish)
                return result

    def feed_fish(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()

                return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                total_fish_price = sum([fish.price for fish in aquarium.fish])
                total_decoration_price = sum([decoration.price for decoration in aquarium.decorations])
                total_price = total_fish_price + total_decoration_price

                return f"The value of Aquarium {aquarium.name} is {total_price:.2f}."

    def report(self):
        result = '\n'.join([str(aquarium) for aquarium in self.aquariums])
        return result
