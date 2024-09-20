"""
Author: Stefan Davis Smith-Steunenberg

More work with classes 
"""
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old, ")

person1 = person("Stefan", 19)
person1.greet()
        