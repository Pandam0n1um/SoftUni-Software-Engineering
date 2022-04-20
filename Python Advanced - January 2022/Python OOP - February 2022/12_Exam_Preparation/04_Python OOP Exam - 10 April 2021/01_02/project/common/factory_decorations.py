from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class FactoryDecoration:
    valid_decorations = {'Ornament': Ornament, 'Plant': Plant}

    def create_decoration(self, decoration_type: str):
        if decoration_type in self.valid_decorations:
            return self.valid_decorations[decoration_type]()
        return None
    # def create_decoration(self, decoration_type: str):
    #     if decoration_type not in self.valid_decorations:
    #         raise ValueError('Invalid decoration type.')
    #     return self.valid_decorations[decoration_type]()