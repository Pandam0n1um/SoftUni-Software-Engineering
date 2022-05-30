class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and roman[value[i]] > roman[value[i - 1]]:
                int_val += roman[value[i]] - 2 * roman[value[i - 1]]
            else:
                int_val += roman[value[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls,value):
        if not isinstance(value,str):
            return "wrong type"

        try:
            return cls(int(value))
        except:
            return "wrong type"