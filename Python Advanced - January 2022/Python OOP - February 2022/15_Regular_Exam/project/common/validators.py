class Validator:
    @staticmethod
    def validate_string_empty_or_whitespace(value: str, error_message):
        if value.strip() == "":
            raise ValueError(error_message)

    @staticmethod
    def validate_value_negative_or_zero(value, error_message):
        if value <= 0:
            raise ValueError(error_message)

    @staticmethod
    def validate_value_negative(value, error_message):
        if value < 0:
            raise ValueError(error_message)

    @staticmethod
    def validate_value_less_than_twelve(value, error_message):
        if value < 12:
            raise ValueError(error_message)

    @staticmethod
    def validate_stamina(value, error_message):
        if not 0 <= value <= 100:
            raise ValueError(error_message)

    @staticmethod
    def raises_if_no_supply_left(type):
        if type == 'Food':
            raise Exception("There are no food supplies left!")
        elif type == 'Drink':
            raise Exception("There are no drink supplies left!")
