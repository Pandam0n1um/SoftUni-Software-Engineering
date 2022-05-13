from abc import ABC, abstractmethod

from project.common.validator import Validator


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name cannot be empty string or white space!"
        Validator.validate_string_empty_or_whitespace(value, error_message)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        error_message = "Price cannot be less than or equal to zero!"
        Validator.validate_value_negative_or_zero(value, error_message)
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
