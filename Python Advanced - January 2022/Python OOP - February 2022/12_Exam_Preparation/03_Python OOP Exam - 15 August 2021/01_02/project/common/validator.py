class Validator:
    @staticmethod
    def validate_string_empty_or_whitespace( value: str, error_message):
        if value.strip() == "":
            raise ValueError(error_message)

    @staticmethod
    def validate_value_negative_or_zero( value, error_message):
        if value <= 0:
            raise ValueError(error_message)

    @staticmethod
    def validate_table_number( value,min_range,max_range, error_message):
        if not min_range <= value <= max_range:
            raise ValueError(error_message)


