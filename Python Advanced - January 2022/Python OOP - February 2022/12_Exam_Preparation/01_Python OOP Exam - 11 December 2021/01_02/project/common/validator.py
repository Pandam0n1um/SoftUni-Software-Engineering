class Validator:
    @staticmethod
    def raise_if_str_length_insuff(value, length, error_message):
        if len(value) < length:
            raise ValueError(error_message)

    @staticmethod
    def raise_if_str_is_empty_or_whitespace(value, error_message):
        if not value.strip():
            raise ValueError(error_message)

    @staticmethod
    def raise_if_str_is_empty(value, error_message):
        if value=='':
            raise ValueError(error_message)

    @staticmethod
    def raise_if_speed_limit_invalid(value, min_speed_limit, max_speed_limit, error_message):
        if not min_speed_limit <= value <= max_speed_limit:
            raise ValueError(error_message)


# if value.strip() =='':
# if len(value.strip()) < 1: