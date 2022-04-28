from abc import ABC, abstractmethod

from project.common.validators import Validator


class BaseFish(ABC):
    SIZE_INCREMENT_EAT = 5

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Fish name cannot be an empty string."
        Validator.validate_string_empty(value, error_message)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        error_message = "Fish species cannot be an empty string."
        Validator.validate_string_empty(value, error_message)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        error_message = "Price cannot be equal to or below zero."
        Validator.validate_value_zero_or_negative(value, error_message)
        self.__price = value

    def eat(self):
        self.size += self.SIZE_INCREMENT_EAT
