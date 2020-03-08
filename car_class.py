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
    def __init__(self, n_passengers, cargo_size, engine_size):
        super().__init__(n_passengers, cargo_size)
        self.engine_size = engine_size

    def park(self):
        return 'Easily'

    def honk(self):
        return 'Loudly'

    def sound(self):
        return 'Decent'

car1 = Vehicle(5, 'Medium')
car2 = Car(7, 'Large', 'V12')

print(car1)
print(car2)

print(car1.accelerate())
print(car1.v_break())

print(car2.sound())
print(car2.accelerate())
