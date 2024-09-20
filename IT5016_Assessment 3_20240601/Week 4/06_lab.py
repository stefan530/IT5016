"""
Author: Stefan Davis Smith-Steunenberg

Lab: passord attempt system that locks out a person after 3 attempts
"""
def password_attempt_system():
  """A simple password attempt system using a while loop."""
  correct_password = "python123"
  attempts = 0
  max_attempts = 3

  while attempts < max_attempts:
    entered_password = input("Enter your password:")
    if entered_password == correct_password:
        print("Access granted! welcome in.")
        break
    else:
        attempts += 1
        print(f"Incorrect password. You have {max_attempts - attempts}attempts left.")
    
    if attempts ==max_attempts:
        print("Access denied. You have used all your attempts")

#running the password attempt system
password_attempt_system()