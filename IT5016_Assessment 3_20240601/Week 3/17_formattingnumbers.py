"""
Author: Stefan Davis Smith-Steunenberg

basic number formatting
"""


pi = 3.141592653589793
formatted_pi = f"Value of pi to 2 decimal places: {pi: .2f}"
print(formatted_pi)

salary=float(input("Enter your salary"))
print(f"Your weekly salary is ${salary:.2f}")