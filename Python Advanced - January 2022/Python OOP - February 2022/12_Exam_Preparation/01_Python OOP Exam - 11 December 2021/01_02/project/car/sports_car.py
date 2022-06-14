from project.car.car import Car


class SportsCar(Car):
    MODEL_MIN_SPEED = 400
    MODEL_MAX_SPEED = 600

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
