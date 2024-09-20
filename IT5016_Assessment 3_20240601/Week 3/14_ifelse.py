"""
Author: Stefan Davis Smith-Steunenberg

Basic definition and explanation of if and else statments

if temperature is greater than 25 ("Wear shorts")
if temperature is lower then 25 ("Wear long pants")
after that value has been checked print enjoy yourself
as the last message

definitions are ignored untill main has been triggerd

"""


def what_to_wear(temperature):
    if temperature > 25:
        print("Wear shorts.")
    else:
        print("Not hot today!")
        print("wear long pants.")
    print("Enjoy yourself.")

def main():
    what_to_wear(20)
    print()
    what_to_wear(30)

main()