from abc import ABC, abstractmethod

from project.common.validator import Validator


class Car(ABC):
    MODEL_MIN_SPEED = 0
    MODEL_MAX_SPEED = 0

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        model_min_length = 4
        error_message = f'Model {value} is less than 4 symbols!'
        Validator.raise_if_str_length_insuff(value, model_min_length, error_message)
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        error_message = f"Invalid speed limit! Must be between {self.MODEL_MIN_SPEED} and {self.MODEL_MAX_SPEED}!"
        Validator.raise_if_speed_limit_invalid(value, self.MODEL_MIN_SPEED, self.MODEL_MAX_SPEED, error_message)
        self.__speed_limit = value

    def __eq__(self, other):
        return self.speed_limit == other.speed_limit

    def __lt__(self, other):
        return self.speed_limit < other.speed_limit
