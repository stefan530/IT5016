"""
Basic minutes/hours calculation display

Author Stefan Davis Smith Steunenberg

"""
def get_minutes(hours, minutes):
    total = hours * 60 + minutes
    return total


hours = float(input("Enter hours"))
minutes= float(input("Enter minutes"))
total_minutes = get_minutes(hours,minutes)

print("The total amount of minutes are", total_minutes)


#print("1.", total_minutes, "minutes")
print("2.", get_minutes(5, 0), "minutes")
print("3.", get_minutes(11, 540), "minutes")

