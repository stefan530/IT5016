"""
Author: Stefan Davis Smith-Steunenberg

Summing up total price and using example usage of a break feature
"""
def calculate_total_amount():
    total_amount = 0.0
    
    while True:
        # Prompt the user to enter the price of an item
        price_input = input("Enter the price of an item (or type 'finish'):").strip()
        
        # Check if the user wants to finish input
        if price_input.lower() == 'finish':
            break
        
        # Try to convert the input to a float and add to total_amount
        try:
            price = float(price_input)
            if price < 0:
                print("Please enter a valid price.")
                continue
            total_amount += price
        except ValueError:
            print("Invalid input'finish' to stop.")
    
    # Display the total amount
    print(f"\nTotal amount: ${total_amount:.2f}")

# Call the function to run the program
calculate_total_amount()