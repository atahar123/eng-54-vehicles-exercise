# import all the classes
from car_class import *
from plane_class import *
from vehicle_class import *

# # create two vehicles
vehicle1 = Vehicle(5, 'Large')
vehicle2 = Vehicle(868, 'Extra Large')


# create two cars instances
# make cars accelerate and make them break
# make car honk and park
car1 = Vehicle('5', 'Medium')
car2 = Car('7', 'Large', 'Mercedes', '512', '185 MPH')

print(car1.accelerate())
print(car1.v_break())

print(car2.honk())
print(car2.park())

# create 2 planes instances
# make planes accelerate and make them break
# make plane fly and land
plane1 = Vehicle('868', 'Very Large')
plane2 = Plane('546', 'Large', 'Trent XWB')

print(plane1.accelerate())
print(plane1.v_break())

print(plane2.take_off())
print(plane2.touch_down())
