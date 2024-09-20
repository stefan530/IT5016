"""
Author: Stefan Davis Smith-Steunenberg

function used to collect user data and display
it in a readable manner
"""
def collect_user_data(id_counter):
    print("Enter user information")
    name = input ("Name:" ).strip()
    age = input("Age: ").strip()
    email = input("Email Address: ").strip
    
    unique_id = id_counter + 1
    id_counter = unique_id

    print(f"\nPrinting Staff Infromation:")
    print(f"Date: {name}")
    print(f"Age: {age}")
    print(f"Email Address: {email}")
    print(f"Unique ID: {unique_id}")

    return id_counter, unique_id, name, age, email,

def main():

    id_counter = 5000
    id_counter, unique_id, name, age ,email = collect_user_data

main()