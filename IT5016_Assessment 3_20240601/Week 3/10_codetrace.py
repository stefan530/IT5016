"""
Basic word length function

Author Stefan Davis Smith Steunenberg

"""
#all of this code is ignored by python until main is triggerd
#if main wasnt started nothing would be printed
#print is inside the def so its ignored

def function1():
    print("A")
    function2(3)
    print("B")

def function2(num):
    print("C")
    function4(num - 1, - 2)
    print("D")

def function3(number):
    print("E", number)

def function4(num1,num2):
    print("F")
    function3(num1 + num2)

def main():
    print("G")
    function1()

main()

#example print stats with G