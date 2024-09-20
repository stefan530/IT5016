#Top class is grandparent
"""
Author: Stefan Davis Smith-Steunenberg

this code shows how inheritance works where car inherits behavior from vehicle aka grandparent
"""
class vehicle():
    def __init__(self) -> None:
        pass
    def start(self):
        print("Vehicle started")
        
    def stop(self):
        print("Vehicle stopped")


#class #new class #Old class        
class Car(vehicle):
    def honk(self):
        print("Honk! Honk!")

my_car = Car()
my_car.start()
my_car.honk()
my_car.stop()

        

        


        
        
        
        
    
        
