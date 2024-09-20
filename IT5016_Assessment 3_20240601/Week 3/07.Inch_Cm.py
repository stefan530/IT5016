"""
inches to cm function

Author Stefan Davis Smith Steunenberg

"""
def inches_to_cm(inches):
    cm = inches * 2.54
    return cm

inches = 10
cm = inches_to_cm(inches)
print(f"{inches} inches is equal to {cm} cm.")
