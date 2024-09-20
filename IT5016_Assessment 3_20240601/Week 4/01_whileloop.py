"""
Author: Stefan Davis Smith-Steunenberg

basic while loop function
"""
def print_lines():                             #Initialisation
    count = 0                                  #count starts at 0?
    while count <100:                          #condition
        print(f"{count} - programming is fun!")#body
        count = count + 1                      #increment

def main():                                    #def main
    print_lines()
main()                                         #main loop