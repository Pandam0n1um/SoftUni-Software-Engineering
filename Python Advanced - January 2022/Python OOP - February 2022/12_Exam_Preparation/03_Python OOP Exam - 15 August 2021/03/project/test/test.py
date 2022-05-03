from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.my_pet_shop = PetShop('TestName')

    def test_init_valid_data(self):
        self.assertEqual('TestName', self.my_pet_shop.name)
        self.assertEqual({}, self.my_pet_shop.food)
        self.assertEqual([], self.my_pet_shop.pets)

    def test_add_food_negative_qty_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.my_pet_shop.add_food('Whiskas', -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_zero_qty_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.my_pet_shop.add_food('Whiskas', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_new_food(self):
        food = 'Whiskas'
        qty = 5
        self.assertEqual({}, self.my_pet_shop.food)
        result = self.my_pet_shop.add_food(food, qty)
        self.assertEqual({food: qty}, self.my_pet_shop.food)
        self.assertEqual(f'Successfully added {qty:.2f} grams of {food}.', result)

    def test_add_food_existing_food(self):
        food = 'Whiskas'
        qty = 500
        self.my_pet_shop.food[food] = qty
        new_qty = 3500
        self.assertEqual({food: qty}, self.my_pet_shop.food)
        result = self.my_pet_shop.add_food(food, new_qty)
        self.assertEqual({food: qty + new_qty}, self.my_pet_shop.food)
        self.assertEqual(f'Successfully added {new_qty:.2f} grams of {food}.', result)

    def test_add_pet(self):
        pet = 'JarJar'
        self.assertEqual([], self.my_pet_shop.pets)
        result = self.my_pet_shop.add_pet(pet)

        self.assertEqual(f'Successfully added {pet}.', result)
        self.assertEqual([pet], self.my_pet_shop.pets)

    def test_add_pet_existing_raises(self):
        self.my_pet_shop.pets = ['JarJar', 'Jawa']
        new_pet = 'JarJar'
        with self.assertRaises(Exception) as ex:
            self.my_pet_shop.add_pet(new_pet)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_missing_pet_raises(self):
        food = 'Whiskas'
        pet = 'Jawa'
        with self.assertRaises(Exception) as ex:
            self.my_pet_shop.feed_pet(food, pet)
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_missing_food_raises(self):
        food = 'Whiskas'
        pet = 'Jawa'
        self.assertEqual({},self.my_pet_shop.food)
        self.my_pet_shop.pets = [pet]
        result=self.my_pet_shop.feed_pet(food, pet)
        self.assertEqual(f'You do not have {food}', result)


    def test_feed_insuff_food_adding(self):
        food = 'Whiskas'
        qty=50
        pet = 'Jawa'
        self.assertEqual({},self.my_pet_shop.food)
        self.my_pet_shop.pets = [pet]
        self.my_pet_shop.food[food]=qty
        result=self.my_pet_shop.feed_pet(food, pet)
        self.assertEqual("Adding food...", result)
        self.assertEqual(qty+1000,self.my_pet_shop.food[food])

    def test_feed_food_suff_and_decreased(self):
        food = 'Whiskas'
        qty=250
        pet = 'Jawa'
        self.assertEqual({},self.my_pet_shop.food)
        self.my_pet_shop.pets = [pet]
        self.my_pet_shop.food[food]=qty
        result=self.my_pet_shop.feed_pet(food, pet)
        self.assertEqual(f"{pet} was successfully fed", result)
        self.assertEqual(qty-100,self.my_pet_shop.food[food])

    def test_repr_dunder(self):
        pets = ['JarJar', 'Jawa']
        self.my_pet_shop.pets = pets
        expected = f'Shop TestName:\n' \
                   f'Pets: {", ".join(pets)}'
        self.assertEqual(expected, str(self.my_pet_shop))



if __name__ == "__main__":
    main()
