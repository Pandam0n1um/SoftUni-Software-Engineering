from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Balkan', 'Dogo', 'Bau-Bau-Bau')

    def test_mammal_init(self):
        self.assertEqual('Balkan', self.mammal.name)
        self.assertEqual('Dogo', self.mammal.type)
        self.assertEqual('Bau-Bau-Bau', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual('Balkan makes Bau-Bau-Bau', result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual('Balkan is of type Dogo', result)


if __name__ == "__main__":
    main()

# class Mammal:
#     def __init__(self, name, mammal_type, sound):
#         self.name = name
#         self.type = mammal_type
#         self.sound = sound
#         self.__kingdom = "animals"
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def get_kingdom(self):
#         return self.__kingdom
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"


# def setUp(self):
# 	name = 'Gosho'
# 	mammal_type = 'Pchela'
# 	sound = 'Bau-Bau'
# 	self.mammal = Mammal(name, mammal_type, sound)
#
# def test_init_parameters_string(self):
# 	self.assertEqual('Gosho', self.mammal.name)
# 	self.assertEqual('Pchela', self.mammal.type)
# 	self.assertEqual('Bau-Bau', self.mammal.sound)
# 	self.assertEqual('animals', self.mammal._Mammal__kingdom)
#
# def test_make_sound(self):
# 	expected = f"Gosho makes Bau-Bau"
# 	actual = self.mammal.make_sound()
#
# 	self.assertEqual(expected, actual)
#
# def test_kingdom_should_return_animals(self):
# 	expected = "animals"
# 	actual = self.mammal.get_kingdom()
#
# 	self.assertEqual(expected, actual)
#
# def test_info_should_return_proper_string(self):
# 	expected = "Gosho is of type Pchela"
# 	actual = self.mammal.info()
#
# 	self.assertEqual(expected, actual)
