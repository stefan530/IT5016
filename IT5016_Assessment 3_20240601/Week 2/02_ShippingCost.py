"""
operation calculate the cost of 60 books

Author Stefan Davis Smith Steunenberg

"""

# Define the variables
book_price = 24.95              # Cover price of the book
discount_rate = 0.40             # Discounted price(40%)
shipping_first_copy = 3.00       # first copy price
shipping_additional_copy = 0.75  # Shipping cost for each additional copy
amount_of_copies = 60            # amount of copies

# Calculate the discounted price of the book
discounted_price = book_price * (1 - discount_rate)

# Calculate the total cost of the books
total_book_cost = discounted_price * amount_of_copies

# Calculate the total shipping cost
# Shipping cost for the first copy
shipping_cost = shipping_first_copy
# Shipping cost for the additional copies
shipping_cost += (amount_of_copies - 1) * shipping_additional_copy

# Calculate the total wholesale cost
total_wholesale_cost = total_book_cost + shipping_cost

#total cost
print("The total cost for 60 books is $", round(total_wholesale_cost, 2))