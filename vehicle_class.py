# define vehicle class here

# characteristics
# n_passengers
# size_cargo

# methods:
# accelerate
# break

class Vehicle():
    # define behaviours and characteristics
    def __init__(self, n_passengers, size_cargo):

    # define the characteristics of every car
        self.n_passengers = n_passengers
        self.size_cargo = size_cargo

    # methods
    def accelerate(self):
        return 'Very quickly'

    def v_break(self):
        return 'In time'

    def sound(self):
        return 'You decide'
