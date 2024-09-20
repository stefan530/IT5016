"""
Author: Stefan Davis Smith-Steunenberg

Random number gueesing game using random import
"""
import random
def user_number_guess(computer_num):
    prompt = "Enter your guess(1-99)"
    num_gueses = 0
    number = 0
    while number != computer_num:
       number = int(input(prompt))
       num_gueses += 1
       if number < computer_num:
         print("too low")
       elif number > computer_num:
         print("too high")
       else:
         print(f"Correct ! number of guess:{num_gueses}")
def main():
    
    user_number_guess(random.randrange(1,100))

main()