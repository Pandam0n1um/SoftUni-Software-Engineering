class Vehicle:

    def __init__(self, veh_type, veh_model, veh_price):
        self.type = veh_type
        self.model = veh_model
        self.price = veh_price
        self.owner = None

    def buy(self, money, owner):
        if not self.owner is None:
            return "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"
        elif money >= self.price:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.type} is owned by: {self.owner}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
