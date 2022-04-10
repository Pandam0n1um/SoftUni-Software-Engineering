from abc import abstractmethod, ABC

from project.common.validators import Validator


class Supply(ABC):
    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name cannot be an empty string."
        Validator.validate_string_empty_or_whitespace(value, error_message)
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        error_message = "Energy cannot be less than zero."
        Validator.validate_value_negative(value, error_message)
        self.__energy = value

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
