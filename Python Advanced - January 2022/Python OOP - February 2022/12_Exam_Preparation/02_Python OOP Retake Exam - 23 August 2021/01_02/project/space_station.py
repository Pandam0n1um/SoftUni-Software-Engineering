from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
	def __init__(self):
		self.astronaut_repository = AstronautRepository()
		self.planet_repository = PlanetRepository()

	def add_astronauts(self, astronaut_type: str, name: str):
		pass

	def add_planet(self, name: str, items: str):
		pass

	def retire_astronaut(self, name: str):
		pass

	def recharge_oxygen():
		pass

	def send_on_mission(self, planet_name: str):
		pass

	def report(self):
		pass