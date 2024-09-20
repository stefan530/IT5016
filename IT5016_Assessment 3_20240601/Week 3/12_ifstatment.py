"""
Author: Stefan Davis Smith-Steunenberg

basic definitions showing how to use if statment to see how to use
if examples to calculate which value is higher then another value

definitions are ignored untill main has been triggerd
"""

def main():
    a = 42
    b = 17
    c= 94
    if a > b and a > c:
        print("You")

    if not (a > b and a >c):
        print("Cannot")

    if a > b or a > c:
        print("Tuna")

    if not (a> b or a >c):
        print("Fish")

main()