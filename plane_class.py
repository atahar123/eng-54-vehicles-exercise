from vehicle_class import *


class Plane(Vehicle):
    def __init__(self, n_passengers, cargo_size, engine_name):
        super().__init__(n_passengers, cargo_size)
        self.engine_name = engine_name

    def take_off(self):
        return 'It\'s hard'

    def touch_down(self):
        return 'At a speed in which it doesn\'t stall'

    def sound(self):
        return 'Very loud'
