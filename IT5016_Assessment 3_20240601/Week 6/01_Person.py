"""
Author: Stefan Davis Smith-Steunenberg

Start of week 6 learning how to use classes to to give 
values to grandchildren 

"""
class person(): # def followed by __init__ alwas followed by starting with self
    def __init__(self, name, age):
        self.name = name #initialize the name attribute
        self.age = age #initialize the age attribute

# Creating instances of the person class
person1 = person("James",30)
person2 = person("Jessica",25)


# Accessing the attributes
print(person1.name) # Output: James
print(person1.age)  # Output: 30
print(person2.name) # Output: Jessica
print(person2.age)  # Output: 25