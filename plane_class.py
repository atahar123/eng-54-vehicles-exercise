from vehicle_class import *


class Plane(Vehicle):
    def __init__(self, n_passengers, cargo_size, engine_size):
        super().__init__(n_passengers, cargo_size)
        self.engine_size = engine_size

    def take_off(self):
        return 'It\'s hard'

    def touch_down(self):
        return 'At a speed in which it doesn\'t stall'

    def sound(self):
        return 'Very loud'


plane1 = Vehicle('868', 'Very Large')
plane2 = Plane('546', 'Large', 'Trent XWB')

print(plane1)
print(plane2)

print(plane1.accelerate())
print(plane1.v_break())

print(plane2.sound())
print(plane2.accelerate())
print(plane2.engine_size)
