"""
Author: Stefan Davis Smith-Steunenberg

Function base around amount of value being over 150 = low or
above 150 = high 
"""
def categorize_request(total_amount):
    # Define the category and recommendation based on total amount
    if total_amount < 150:
        category = "low"
        recommendation = "Recommended: Proceed with standard processing."
    else:
        category = "high"
        recommendation = "Recommended: Review for potential discounts."
    
    # Print the summary
    print(f"Request Summary:")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Category: {category.capitalize()}")
    print(f"Recommendation: {recommendation}")

# Example usage
try:
    total_amount = float(input("Enter the total amount: "))
    categorize_request(total_amount)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
