from project.common.validator import Validator


class Planet:
	def __init__(self, name: str):
		self.name = name
		self.items = []

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		error_message = "Planet name cannot be empty string or whitespace!"
		Validator.raise_if_str_is_empty_or_whitespace(value, error_message)
		self.__name=value
	pass
