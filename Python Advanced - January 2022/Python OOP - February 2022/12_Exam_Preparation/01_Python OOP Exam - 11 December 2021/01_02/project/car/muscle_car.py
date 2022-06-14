from project.car.car import Car


class MuscleCar(Car):
    MODEL_MIN_SPEED = 250
    MODEL_MAX_SPEED = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

