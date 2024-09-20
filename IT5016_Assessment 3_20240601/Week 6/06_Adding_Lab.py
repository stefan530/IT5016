"""
Author: Stefan Davis Smith-Steunenberg

More detailed version of the previous lab with added values/details
"""
class Car:
    def __init__(self,color,model,display,year):
        self.color = color
        self.model = model
        self.display = display
        self.year = year
      
    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")
    
    def info(self):
        print(f"Car Info:{self.year} {self.color} {self.model} {self.display} ")

#Creating instances of the car class.

car1 = Car("Blue","Ford","Mustang","")
car1 = Car("Blue","Ford","Mustang","")
car2 = Car("2021","Blue","Ford","Mustang")

# Call methods on the instances

car1.drive() #Output: The blue ford mustang is driving.
car1.stop()  #Output: The blue ford mustang has stopped
car2.info()

#car2.display() #Output: Car Info: 2021 blue ford mustang



