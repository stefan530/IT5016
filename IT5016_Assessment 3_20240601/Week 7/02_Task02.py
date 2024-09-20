"""
Author: Stefan Davis Smith-Steunenberg

Task 2:

code showing a basic implementation of a student membership system, using basic object-oriented programming
"""
class Student:
    def __init__(self, student_id, last_name, programme):
        self.student_id = student_id
        self.last_name = last_name
        self.programme = programme
        self.membership_id = None

    def __str__(self):
        return f"ID: {self.student_id}, Last Name: {self.last_name}, Programme: {self.programme}, Membership ID: {self.membership_id}"


class MembershipSystem:
    def __init__(self):
        self.students = {}
        self.next_membership_id = 1
        self.num_registered_members = 0

    def register_student(self, student_id, last_name, programme):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return

        new_student = Student(student_id, last_name, programme)
        new_student.membership_id = self.next_membership_id
        self.students[student_id] = new_student

        print(f"Student {last_name} registered successfully with Membership ID: {self.next_membership_id}.")
        self.next_membership_id += 1
        self.num_registered_members += 1

    def withdraw_membership(self, student_id):
        if student_id not in self.students:
            print("No student found with this ID.")
            return

        student = self.students.pop(student_id)
        self.num_registered_members -= 1

        print(f"Membership withdrawn for student {student.last_name}.")
        print(f"Updated number of registered members: {self.num_registered_members}")

    def get_student_info(self, student_id):
        if student_id in self.students:
            return str(self.students[student_id])
        else:
            return "No student found with this ID."


# Example
if __name__ == "__main__":
    system = MembershipSystem()

    # Register 
    system.register_student(1, "Smith", "Bachelor")
    system.register_student(2, "Johnson", "Diploma")

 
    print(system.get_student_info(1))
    print(system.get_student_info(2))


    system.withdraw_membership(1)

   
    print(system.get_student_info(1))
