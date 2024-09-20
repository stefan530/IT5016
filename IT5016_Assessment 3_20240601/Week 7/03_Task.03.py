"""
Author: Stefan Davis Smith-Steunenberg

Task 3:

code showing a functional framework for a request management system, showing key object-oriented programming concepts such as class attributes.
"""
class RequestSystem:
    unique_id_counter = 1  
    
    def __init__(self):
        self.requests = []
        self.total_requests = 0
        self.approved_requests = 0
        self.pending_requests = 0
        self.not_approved_requests = 0

    def user_info(self, name, age, email, request_details, item_list):
        """ Collects user details and calculates the total amount for request items """
        total_cost = sum(cost for item, cost in item_list)
        request_id = RequestSystem.unique_id_counter
        RequestSystem.unique_id_counter += 1
        
        request = {
            'request_id': request_id,
            'name': name,
            'age': age,
            'email': email,
            'request_details': request_details,
            'items': item_list,
            'total_amount': total_cost,
            'status': 'Pending'
        }
        
        self.requests.append(request)
        self.total_requests += 1
        self.pending_requests += 1

        return total_cost, item_list

    def request_approval(self, request_id):
        """ Determines if a request is approved based on the total amount """
        for request in self.requests:
            if request['request_id'] == request_id:
                if request['total_amount'] < 150:
                    request['status'] = 'Approved'
                    self.approved_requests += 1
                else:
                    request['status'] = 'Pending'
                return

    def respond_request(self, request_id, approved):
        """ Allows a manager to respond to a pending request """
        for request in self.requests:
            if request['request_id'] == request_id:
                if request['status'] == 'Pending':
                    if approved:
                        request['status'] = 'Approved'
                        self.approved_requests += 1
                    else:
                        request['status'] = 'Not Approved'
                        self.not_approved_requests += 1
                    self.pending_requests -= 1
                return

    def display_request(self):
        """ Prints details for all requests """
        for request in self.requests:
            print(f"ID: {request['request_id']}, Name: {request['name']}, Total: {request['total_amount']}, Status: {request['status']}")

    def request_static(self):
        """ Displays statistical information about the requests """
        print(f"Total Requests Submitted: {self.total_requests}")
        print(f"Total Approved Requests: {self.approved_requests}")
        print(f"Total Pending Requests: {self.pending_requests}")
        print(f"Total Not Approved Requests: {self.not_approved_requests}")

# Example usage
if __name__ == "__main__":
    system = RequestSystem()

    # Submit requests
    system.user_info('James Bond', 30, 'James@bond.com', 'Office Supplies', [('Pens', 20), ('Notebooks', 50)])
    system.user_info('Bond James', 40, 'bond@james.com', 'Computers', [('Laptop', 300), ('Mouse', 20)])

    # Process requests
    system.request_approval(1)  # ID 1 has a total cost of 70, which is less than 150, so it's approved
    system.respond_request(2, approved=False)  # ID 2 has a total cost of 320, which is greater than 150

    # Display all requests
    system.display_request()

    # Display request statistics
    system.request_static()
