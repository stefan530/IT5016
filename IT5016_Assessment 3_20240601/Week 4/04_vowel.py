"""
Author: Stefan Davis Smith-Steunenberg

Vowel counting function
"""
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text:
        if char.lower() in vowels:
            count += 1
    return count

def main():
    text = input("Enter the text: ")  # Added space after prompt for clarity
    vowel_count = count_vowels(text)  # Call the function with the input text
    print(f"Number of vowels in '{text}': {vowel_count}")

main()