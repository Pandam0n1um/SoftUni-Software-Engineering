from project.common.validators import Validator


class Player:
    CREATED_PLAYERS = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name not valid!"
        Validator.validate_string_empty_or_whitespace(value, error_message)
        if value in Player.CREATED_PLAYERS:
            raise Exception(f"Name {value} is already used!")

        Player.CREATED_PLAYERS.append(value)
        self.__name = value

    # TODO exception existing player name - add functionality-DONE MAYBE??

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        error_message = "The player cannot be under 12 years old!"
        Validator.validate_value_less_than_twelve(value, error_message)
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        error_message = "Stamina not valid!"
        Validator.validate_stamina(value, error_message)
        self.__stamina = value

    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True
        return False

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def __lt__(self, other):
        return self.stamina < other.stamina
