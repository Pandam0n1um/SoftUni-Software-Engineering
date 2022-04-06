class Validator:


    @staticmethod
    def raise_if_value_negative(value,error_message):
        if value<0:
            raise ValueError(error_message)