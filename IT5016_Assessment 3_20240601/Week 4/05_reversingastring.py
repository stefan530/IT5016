"""
Author: Stefan Davis Smith-Steunenberg

function reversing a string
"""
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    original_string = input("Enter a string: ")
    reversed_string = reverse_string(original_string)
    print(f"Original: {original_string}")
    print(f"Reversed: {reversed_string}")

main()