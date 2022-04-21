class Validator:

    @staticmethod
    def validate_string_empty(value: str, error_message):
        if value == "":
            raise ValueError(error_message)

    @staticmethod
    def validate_value_zero_or_negative(value: str, error_message):
        if value <= 0:
            raise ValueError(error_message)
