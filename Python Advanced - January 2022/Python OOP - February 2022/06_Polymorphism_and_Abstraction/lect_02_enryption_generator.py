class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        result = ""
        for letter in self.text:
            new_ascii = ord(letter) + other
            while new_ascii > 126:
                new_ascii -= 95
            while new_ascii < 32:
                new_ascii += 95
            result += chr(new_ascii)
        return result


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
