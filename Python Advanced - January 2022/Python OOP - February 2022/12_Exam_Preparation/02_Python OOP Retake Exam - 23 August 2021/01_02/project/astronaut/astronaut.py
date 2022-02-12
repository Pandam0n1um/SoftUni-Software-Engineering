from abc import ABC, abstractmethod

from project.common.validator import Validator


class Astronaut(ABC):
	@abstractmethod
	def __init__(self, name: str, oxygen: int):
		self.name = name
		self.oxygen = oxygen
		self.backpack = []

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value: str):
		error_message = "Astronaut name cannot be empty string or whitespace!"
		Validator.raise_if_str_is_empty_or_whitespace(value, error_message)
		self.__name = value

	def breathe(self):
		self.oxygen -= 10

	def increase_oxygen(self, amount: int):
		self.oxygen += amount
