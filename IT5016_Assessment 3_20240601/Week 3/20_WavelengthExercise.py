"""
Author: Stefan Davis Smith-Steunenberg

First "lab" using basic if elif conditions to check the value and put it
in a category from 380-750
"""
def main():
    print("welcome to the wavelength to color converter")
    print("please enter an integer wavelength between 380 and 750 nm")

    try:
        # Reading wavelength the user provides
        wavelength = int(input("Enter wavelength in nm:"))

        # Determine the color
        
        # if elif
        if 380 <= wavelength < 450:
            color = "Violet"
        
        elif 450 <= wavelength < 495:
            color = "bBlue"
        
        elif 495 <= wavelength < 570:
            color = "green"
        
        elif 570 <= wavelength < 590:
            color = "yelloow"
        
        elif 590 <= wavelength < 620:
            color = "orange"
        
        elif 620 <= wavelength <= 750:
            color = "red"
        
        else:
            color = None

        # outputing the final result
        if color:
            
            print(f"thank you the wavelength that you entered in nanometers is {wavelength}.")
            print(f"The color for this wavelength is {color}")
        else:
            print("The wavelength is outside the spectrum")
    
    except ValueError:
        print("invalid input please enter a accepeted value")

if __name__ == "__main__":
    main()