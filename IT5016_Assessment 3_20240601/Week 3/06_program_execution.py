"""
program execution

Author Stefan Davis Smith Steunenberg

"""
def display_intro():
    message = "Game of Nim"
    print(message)

def display_winner_details(winner,score):
    message = "***" + winner.upper() + "(" + str(score) +\
                                                    ") ***"

                                                   