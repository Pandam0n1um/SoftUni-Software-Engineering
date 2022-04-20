from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class FactoryAquarium:
    valid_aquariums = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium
    }

    # def create_aquarium(self, aquarium_type, name):
    #     if aquarium_type in self.valid_aquariums:
    #         return self.valid_aquariums[aquarium_type](name)
    #     return None
    def create_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.valid_aquariums:
            raise ValueError('Invalid aquarium type.')
        return self.valid_aquariums[aquarium_type](aquarium_name)