"""
celsius to fahrenheit

Author: Stefan Davis Smith Steunenberg

"""
def celsius_to_f(celsius):
    #celsius to fahrenheit: F=(C x 9/5) + 32
    fahrenheit = celsius * 9 / 5 + 32 
    return fahrenheit


celsius = float(input("Enter celsius:"))
print("1.","Celsius",celsius,"= Fahrenheit",celsius_to_f(celsius))

celsius = float(input("Enter celsius:"))
print("2.","Celsius",celsius,"= Fahrenheit",celsius_to_f(celsius))

celsius = float(input("Enter celsius"))
print("3.","Celsius",celsius,"= Fahrenheit",celsius_to_f(celsius))