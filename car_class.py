# import my vehicle class

# define car class here and make it in inherit from vehicle

# characteristics
# brand
# horsepower
# max_speed

# methods:
# park
# honk

from vehicle_class import *


class Car(Vehicle):
    def __init__(self, n_passengers, cargo_size, brand, horsepower, max_speed):
        super().__init__(n_passengers, cargo_size)
        self.brand = brand
        self.horsepower = horsepower
        self.max_speed = max_speed

    def park(self):
        return 'Easily'

    def honk(self):
        return 'Loudly'

    def sound(self):
        return 'Decent'

