from project.common.validator import Validator


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        error_message = 'Name should contain at least one character!'
        Validator.raise_if_str_is_empty_or_whitespace(value, error_message)
        self.__name = value
