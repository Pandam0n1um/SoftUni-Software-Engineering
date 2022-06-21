from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    car_types_map = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        if car_type in Controller.car_types_map:
            new_car = Controller.car_types_map[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__find_driver(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race_name == race.name:
                raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        curr_driver = self.__find_driver(driver_name)
        if not curr_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        new_car = self.__find_free_car(car_type)

        if curr_driver.car:
            old_car = curr_driver.car
            curr_driver.car = new_car
            old_car.is_taken = False
            curr_driver.car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."

        curr_driver.car = new_car
        curr_driver.car.is_taken = True
        return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        curr_race = self.__find_race(race_name)
        if not curr_race:
            raise Exception(f"Race {race_name} could not be found!")

        curr_driver = self.__find_driver(driver_name)
        if not curr_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not curr_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if curr_driver in curr_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        curr_race.drivers.append(curr_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        curr_race = self.__find_race(race_name)
        if not curr_race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(curr_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners_list = sorted(curr_race.drivers, key=lambda x: x.car, reverse=True)[:3]
        for winner in winners_list:
            winner.number_of_wins += 1

        result = '\n'.join(
            [f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}." for
             winner in winners_list])
        return result

    def __find_driver(self, driver_name):
        for driver in self.drivers:
            if driver_name == driver.name:
                return driver
        return None

    def __find_free_car(self, car_type):
        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def __find_race(self, race_name):
        for race in self.races:
            if race_name == race.name:
                return race
        return None
