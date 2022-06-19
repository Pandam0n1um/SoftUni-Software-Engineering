class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):
    def setUp(self):
        self.list_integers = IntegerList(4, 5, 6)

    def test_initialization_without_data(self):
        integer_list = IntegerList()
        self.assertEqual([], integer_list._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_data(self):
        integer_list = IntegerList(3, 4, 'wrong_input', 6)
        self.assertEqual([3, 4, 6], integer_list._IntegerList__data)

    def test_is_initialized_correctly_with_correct_data(self):
        integer_list = IntegerList(5, 'wrong_input')
        self.assertEqual([5], integer_list._IntegerList__data)

    def test_get_method(self):
        actual_output = self.list_integers.get_data()
        self.assertEqual([4, 5, 6], actual_output)

    def test_add_valid_element(self):
        result = self.list_integers.add(7)
        self.assertEqual([4, 5, 6, 7], result)

    def test_add_invalid_element_raises(self):
        with self.assertRaises(Exception) as ex:
            self.list_integers.add(6.5)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_remove_element_valid_index(self):
        result = self.list_integers.remove_index(2)
        self.assertEqual(6, result)

    def test_remove_element_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_element_valid_index(self):
        result = self.list_integers.get(2)
        self.assertEqual(6, result)

    def test_get_element_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_element_valid_index(self):
        self.list_integers.insert(1, 3)
        self.assertEqual([4, 3, 5, 6], self.list_integers._IntegerList__data)

    def test_insert_element_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.insert(5, 3)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_element_invalid_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.insert(2,3.14)
        self.assertEqual("Element is not Integer",str(ex.exception))

    def test_get_biggest_number(self):
        result=self.list_integers.get_biggest()
        self.assertEqual(6,result)

    def test_get_index_of_element(self):
        result=self.list_integers.get_index(4)
        self.assertEqual(0,result)

if __name__ == '__main__':
    main()
