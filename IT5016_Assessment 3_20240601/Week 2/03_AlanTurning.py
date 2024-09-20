"""
lab 3
Author Stefan Davis Smith Steunenberg

"""

name = "Alan Turning"
#name = str(input("Enter the name:"))
extras = 3

name_length = len(name)
stars_length = name_length + extras * 2
print("*" * stars_length)
print("" *extras + name + "" * extras)
print("*" * stars_length)