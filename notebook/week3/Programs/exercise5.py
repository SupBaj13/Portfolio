
# Exercise 5: Password with repeated attempts
print("\n=== Exercise 5: Password with Repeated Attempts ===")
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password (8-12 characters): ")
    password2 = input("Enter the password again: ")
    
    if password1 != password2:
        print("Error: Passwords do not match")
        continue
    
    if len(password1) < 8 or len(password1) > 12:
        print("Error: Password must be between 8 and 12 characters long")
        continue
    
    if password1 in BAD_PASSWORDS:
        print("Error: Password is too common. Choose a different one.")
        continue
    
    print("Password Set")
    break