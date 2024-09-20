"""
Author: Stefan Davis Smith-Steunenberg

Extended usage of classes to try and understand 
the uses of classes
"""
class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.model} is driving. ")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

# Creating instances of the car class.
car1 = Car("red","Toyota")
car2 = Car("blue","Honda")

# Call methods on the instances
car1.drive() #Output: The red Toyota is driving.
car1.stop()  #Output: The red Toyota has stopped.

car2.drive() #Output: The blue honda is driving.
car2.stop()  #Output: The blue honda has stopped.