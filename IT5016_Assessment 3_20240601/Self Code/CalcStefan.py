"""
Author: Stefan Davis Smith-Steunenberg

This is more of a basic function i would be able to create as compared to the other one,

"""
def calculator():
    print("Welcome to the Basic Calculator!")
    print("Enter two numbers and an operator (+, -, *, /)")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero."
    else:
        result = "Invalid operator."

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()