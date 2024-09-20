"""
Author: Stefan Davis Smith-Steunenberg

While loop extended
"""
def ShoppingList():
    total = 0
    number = float(input("Enter a number(0 to end):  "))
    while number !=0:
        total += number
        number = float(input("Enter a number(0 to end):  "))

    print("Total:: ",total)
def main():
    ShoppingList()

main()