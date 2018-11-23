#Lesson with variables
cars = 100
space_in_a_car = 4.0
drivers = 30
pasangers = 90
#This will help us to know how much cars do not race today
cars_not_driven = cars - drivers
#Only car with driver can drive
car_driven = drivers
#So we need to know how much peopel we can transport
carpool_capacity = cars * space_in_a_car
#And per car this should be
averege_pasangers_per_car = pasangers / car_driven

print("There are", cars, "cars available.")
print("There are", drivers, "drivers available.")
print("There will be", cars_not_driven, "cars empty today.")
print("We can transport", carpool_capacity, "peopel today.")
print("We have", pasangers, "to carpool today.")
print("We need to put about", averege_pasangers_per_car, "in each car.")
