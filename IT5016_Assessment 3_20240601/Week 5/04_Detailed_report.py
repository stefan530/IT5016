"""
Author: Stefan Davis Smith-Steunenberg

Semi detailed report with total amount, user infromation all printed out
in a pretty function
"""
def collect_user_data(id_counter):
    print("Enter user information")
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    email = input("Email Address: ").strip()
    
    # Increment the id_counter and use it as the unique ID
    unique_id = id_counter + 1
    
    return unique_id, name, age, email

def calculate_total_amount():
    total_amount = 0.0
    
    while True:
        # Prompt the user to enter the price of an item
        price_input = input("Enter the price of an item (or type 'finish' to stop): ").strip()
        
        # Check if the user wants to finish input
        if price_input.lower() == 'finish':
            break
        
        # Try to convert the input to a float and add to total_amount
        try:
            price = float(price_input)
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            total_amount += price
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    return total_amount

def categorize_request(total_amount):
    # Define the category and recommendation based on total amount
    if total_amount < 150:
        category = "low"
        recommendation = "Recommended: Proceed with standard processing."
    else:
        category = "high"
        recommendation = "Recommended: Review for potential discounts."
    
    return category, recommendation

def create_detailed_report(id_counter):
    # Collect user data
    unique_id, name, age, email = collect_user_data(id_counter)
    
    # Calculate total amount
    total_amount = calculate_total_amount()
    
    # Categorize the request
    category, recommendation = categorize_request(total_amount)
    
    # Print the detailed report
    print("\nDetailed Report:")
    print(f"Unique ID: {unique_id}")
    print(f"Username: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Category: {category.capitalize()}")
    print(f"Recommendation: {recommendation}")

def main():
    # Initialize the id_counter
    id_counter = 5000
    
    # Create and display the detailed report
    create_detailed_report(id_counter)

# Run the main function
main()