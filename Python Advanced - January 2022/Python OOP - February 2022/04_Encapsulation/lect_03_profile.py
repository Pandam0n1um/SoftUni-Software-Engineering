# class Profile:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         if not 5 <= len(value) <= 15:
#             raise ValueError("The username must be between 5 and 15 characters.")
#         self.__username = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         if self.is_length_valid(value) and self.contains_number(value) and self.contains_uppercase(value):
#             self.__password=value
#             return
#         raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#
#     def is_length_valid(self, password):
#         return len(password) >= 8
#
#     def contains_uppercase(self, password):
#         upper_letters = [char for char in password if char.isupper()]
#         return True if upper_letters else False
#
#     def contains_number(self, password):
#         return password.isalnum()
#
#     def __str__(self):
#         return f"You have a profile with username: \"{self.username}\" and password: {len(self.password)*'*'}"
#
class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 < len(value) < 15:
            self.__username = value
        raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_upper_case = any([True for char in value if char.isupper()])
        is_digit = any([True for char in value if char.isdigit()])

        if is_length_valid and is_upper_case and is_digit:
            self.__password = value
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')

# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
