"""
Basic code tracing

Author Stefan Davis Smith Steunenberg

"""
#functions work by being ignored by the code until the python
#program enocunters a situation in where it needs to be used
#years = age so + 10 to age to get the value to print in fun_2
def fun_2(age):
    years = age + 10
    print("3.", years)

def fun_1(years_):
    print("4.", years)
    years = 20

def main():
    years = 5
    fun_1(years)
    print("1.", years)
    fun_2(years)
    print("2.",years)


main()