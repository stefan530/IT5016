"""
Author: Stefan Davis Smith-Steunenberg

Collecting user data and creating a unique id + 1
"""
#Task 1:
def Staff_info(unique_id):
    print("Printing Staff Information:")
    date = input("Date:").strip()
    staff_id = input("Staff ID:").strip()
    staff_Name = input("Staff Name:").strip()
    requisition_id = input("Requisition_ID:").strip()
    
    # Increment the requisition_id and use it as the unique ID
    requisition_id = unique_id + 1
    
    print(f"\nUser Information:")
    print(f"Date: {date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_Name}")
    print(f"Requisition ID: {requisition_id}")

    # Return the updated id_counter and the unique ID with user information
    return date, staff_id, staff_Name, requisition_id

def main():
    # Initialize the id_counter
    requisition_id = 10000
    
    # Call the collect_user_data function and unpack the returned values
    unique_id, name, age, email = Staff_info(requisition_id)

    Uniquie_staff_id = ()
    
    # Update the id_counter with the new value
    requisition_id = unique_id
    
main()

