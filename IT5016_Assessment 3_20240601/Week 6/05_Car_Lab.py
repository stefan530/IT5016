"""
Author: Stefan Davis Smith-Steunenberg

Lab 1 of week 6, we were tasked with creating this function
"""
class Car:
    def __init__(self,color,model,year):
        self.color = color
        self.model = model
        self.year = year

        print(f"{self.color}") 
        print(f"{self.model}")
        print(f"{self.year}")

# Creating instances of the car class.
car1 = Car("Black","Tesla Model S","2023")

