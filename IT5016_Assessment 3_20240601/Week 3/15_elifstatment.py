"""
Author: Stefan Davis Smith-Steunenberg

Basic definition and explanation of if elif and else statments

prompting a selection of 3 options from the user and display
a differenet message for each of the inputs the user makes

Example 
inputing 1 will say time to east
inputing 2 will say time to play
inputing 3 will say time to sleep

"""


def what_to_do_now():
    message = "Time to "
    prompt = "Enter selection (1, 2, or 3): "
    user_choice = int(input(prompt))

    if user_choice ==1:
        print(message,"eat")
    elif user_choice ==2:
        print(message,"play")
    elif user_choice ==3:
        print(message,"sleep")
    else:
        print("incorrect selection:")

what_to_do_now()