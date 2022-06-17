class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Balkan")

    def test_correct_initialization(self):
        self.assertEqual('Balkan', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_eat_fed_raises(self):
        # Arrange
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        # Act
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        # Assert
        expected = "Already fed."
        self.assertEqual(expected, str(ex.exception))

    def test_cat_sleepy_after_eat(self):
        # Arrange
        self.assertFalse(self.cat.sleepy)
        # Act
        self.cat.eat()
        # Assert
        self.assertTrue(self.cat.sleepy)

    def test_cat_fed_after_eat(self):
        # Arrange
        self.assertFalse(self.cat.fed)
        # Act
        self.cat.eat()
        # Assert
        self.assertTrue(self.cat.fed)

    def test_cat_size_increase_after_eat(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.cat.fed = False
        self.assertEqual(1, self.cat.size)
        self.cat.eat()
        self.assertEqual(2, self.cat.size)

    def test_cat_sleep_if_not_fed_raises(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        expected = 'Cannot sleep while hungry'
        self.assertEqual(expected, str(ex.exception))

    def test_cat_sleep_if_fed(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    main()

# from unittest import TestCase, main
#
# class CatTests(TestCase):
# 	def setUp(self):
# 		self.cat = Cat("Balkan")
#
# 	def test_init_creates_all_attributes(self):
# 		# Arrange and Act
# 		# Assert
# 		self.assertEqual('Balkan', self.cat.name)
# 		self.assertFalse(self.cat.sleepy)
# 		self.assertFalse(self.cat.fed)
# 		self.assertEqual(0, self.cat.size)
#
# 	def test_is_cat_siZe_increased_after_eating(self):
# 		# Arrange and Act
# 		# Assert
# 		self.assertEqual(0, self.cat.size)
# 		self.cat.eat()
# 		self.assertEqual(1, self.cat.size)
#
# 	def test_is_cat_fed_after_eating(self):
# 		self.assertFalse(self.cat.fed)
# 		self.cat.eat()
# 		self.assertTrue(True, self.cat.fed)
#
# 	def test_cat_can_not_eat_if_fed_raises(self):
# 		self.assertFalse(self.cat.fed)
# 		self.cat.eat()
# 		with self.assertRaises(Exception) as ex:
# 			self.cat.eat()
# 		self.assertEqual('Already fed.', str(ex.exception))
#
# 	def test_cat_can_not_fall_asleep_if_not_fed_raises(self):
# 		self.assertFalse(self.cat.fed)
# 		with self.assertRaises(Exception) as ex:
# 			self.cat.sleep()
# 		self.assertEqual("Cannot sleep while hungry", str(ex.exception))
#
# 	def test_cat_not_sleepy_after_sleeping(self):
# 		self.cat.eat()
# 		self.assertTrue(self.cat.sleepy)
# 		self.cat.sleep()
# 		self.assertFalse(self.cat.sleepy)
#
#
# if __name__ == '__main__':
# 	main()
