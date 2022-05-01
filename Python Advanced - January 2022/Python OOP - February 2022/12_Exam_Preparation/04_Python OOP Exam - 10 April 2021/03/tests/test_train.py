from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train('Thomas', 2)

    def test_valid_data_init(self):
        self.assertEqual('Thomas', self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passengers_insuff_capacity(self):
        self.train.passengers = ['Harry', 'Ron']
        with self.assertRaises(ValueError) as ex:
            self.train.add('Hermione')
        self.assertEqual('Train is full', str(ex.exception))

    def test_add_passengers_existing_passenger_raises(self):
        self.train.passengers = ['Harry', ]
        new_passenger = 'Harry'
        with self.assertRaises(ValueError) as ex:
            self.train.add(new_passenger)
        self.assertEqual(f'Passenger {new_passenger} Exists', str(ex.exception))

    def test_add_passenger_valid_scenario(self):
        self.train.passengers = ['Harry', ]
        new_passenger = 'Ron'
        result=self.train.add(new_passenger)
        self.assertEqual(f"Added passenger {new_passenger}", result)

    def test_remove_passenger_not_existing_raises(self):
        self.train.passengers = ['Harry', 'Ron']
        with self.assertRaises(ValueError) as ex:
            self.train.remove('Hermione')
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_passenger_valid_scenario(self):
        self.train.passengers = ['Harry', ]
        passenger = 'Harry'
        result=self.train.remove(passenger)
        self.assertEqual(f"Removed {passenger}", result)



if __name__ == '__main__':
    main()
