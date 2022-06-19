from project.vehicle import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
	def setUp(self):
		self.vehicle = Vehicle(34.5,222.2)

	def test_init_valid_data(self):
		self.assertEqual(34.5,self.vehicle.fuel)
		self.assertEqual(34.5,self.vehicle.capacity)
		self.assertEqual(222.2,self.vehicle.horse_power)
		self.assertEqual(1.25,self.vehicle.fuel_consumption)


	def test_drive_enough_fuel(self):
		self.vehicle.drive(2)
		self.assertEqual(32,self.vehicle.fuel)


	def test_drive_not_enough_fuel(self):
		with self.assertRaises(Exception) as ex:
			self.vehicle.drive(100)
		self.assertEqual('Not enough fuel',str(ex.exception))

	def test_refuel_within_capacity(self):
		self.assertEqual(34.5,self.vehicle.fuel)
		self.assertEqual(34.5,self.vehicle.capacity)
		self.vehicle.drive(2)
		self.assertEqual(32,self.vehicle.fuel)
		self.vehicle.refuel(2.5)
		self.assertEqual(34.5,self.vehicle.fuel)

	def test_refuel_beyond_capacity_raises(self):
		self.assertEqual(34.5,self.vehicle.fuel)
		self.assertEqual(34.5,self.vehicle.capacity)
		self.vehicle.drive(2)
		self.assertEqual(32,self.vehicle.fuel)
		with self.assertRaises(Exception) as ex:
			self.vehicle.refuel(3)
		self.assertEqual('Too much fuel',str(ex.exception))

	def test_str_dunder(self):
		expected= f"The vehicle has 222.2 horse power with 34.5 fuel left and 1.25 fuel consumption"
		self.assertEqual(expected,str(self.vehicle))

if __name__ == "__main__":
	main()

#
# class Vehicle:
# 	DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
# 	fuel_consumption: float
# 	fuel: float
# 	capacity: float
# 	horse_power: float
#
# 	def __init__(self, fuel: float, horse_power: float):
# 		self.fuel = fuel
# 		self.capacity = self.fuel
# 		self.horse_power = horse_power
# 		self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
#
# 	def drive(self, kilometers):
# 		fuel_needed = self.fuel_consumption * kilometers
# 		if self.fuel < fuel_needed:
# 			raise Exception("Not enough fuel")
# 		self.fuel -= fuel_needed
#
# 	def refuel(self, fuel):
# 		if self.fuel + fuel > self.capacity:
# 			raise Exception("Too much fuel")
# 		self.fuel += fuel
#
# 	def __str__(self):
# 		return f"The vehicle has {self.horse_power} " \
# 			   f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
