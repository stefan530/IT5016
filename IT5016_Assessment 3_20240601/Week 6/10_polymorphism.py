"""
Author: Stefan Davis Smith-Steunenberg

function demonstarting basic polmorphism where different devices use the same method in their own way
"""
#Defining the base class
class Device():
    def turn_on(self):
        pass
class TV(Device):
    def turn_on(self):
        return "TV is now on"
class Fan(Device):
    def turn_on(self):
        return "The light is on"
class Light(Device):
    def turn_on(self):
        return "Light is now on"       

def activate_device(device):
    print(device.turn_on())
    
tv = TV()
fan = Fan()
light = Light()

activate_device(tv)
activate_device(fan)
activate_device(light)
    