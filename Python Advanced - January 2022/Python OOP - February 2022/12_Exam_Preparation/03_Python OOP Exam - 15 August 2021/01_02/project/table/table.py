from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.common.validator import Validator
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.validate_table_number(
            value,
            self.min_table_number,
            self.max_table_number,
            self.table_number_error_message
        )

        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        error_message = "Capacity has to be greater than 0!"
        Validator.validate_value_negative_or_zero(value, error_message)
        self.__capacity = value

    @property
    @abstractmethod
    def min_table_number(self):
        pass

    @property
    @abstractmethod
    def max_table_number(self):
        pass

    @property
    @abstractmethod
    def table_number_error_message(self):
        pass

    def reserve(self, number_of_people: int):
        self.is_reserved=True
        self.number_of_people=number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(x.price for x in self.food_orders)+sum(x.price for x in self.drink_orders)

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
