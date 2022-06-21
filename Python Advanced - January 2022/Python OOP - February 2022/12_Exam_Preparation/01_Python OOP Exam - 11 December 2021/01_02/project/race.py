from project.common.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = 'Name cannot be an empty string!'
        Validator.raise_if_str_is_empty(value, error_message)
        self.__name = value

