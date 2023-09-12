"""
Name: Alysha Marin
M03_Lab.py
This Python app allows users to input and store information about a car, 
including its year, make, model, number of doors, and type of roof. 
The app uses two classes, Vehicle and Automobile, to organize and
display the data to the user. 
"""

# super class 
class Vehicle: 
    # initialize the 'Vehicle' class with user input for vehicle type 
    def __init__(self):
        self.vehicleType = input("what type of vehicle do you have?")
    def vehicle_display(self):
        print("Vehicle: ", self.vehicleType)

# sub class that inherits from super class 'Vehicle'.
class Automobile(Vehicle):
    # initialize the 'Automobile' class with user inputs for vehicle attributes
    def __init__ (self):
        self.year = input("What is the vehicle's year? ")
        self.make = input("What is the vehicle's make? ")
        self.model = input("What is the vehice's model? ")
        self.door = input("How many doors does this vehicle's door?")
        self.roof = input("What type of roof does this vehicle have?")

    # method to display automobile attributes
    def car_display(self):
        print("\nYear: ", self.year, "\nMake: ", self.make, "\nModel: ", self.model, "\nNumber of door: ", self.door, "\nType of roof: ", self.roof)

# prompts the user to enter vehicle type with this instance
user_vehicle = Vehicle()
# prompts the user to enter automobile attributes with this instance
user_automobile = Automobile()
# display vehicle type 
user_vehicle.vehicle_display()
# display automobile attributes 
user_automobile.car_display()


