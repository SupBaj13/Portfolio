
# Exercise 4: Password with common password check
print("\n=== Exercise 4: Password with Common Password Check ===")
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter a new password (8-12 characters): ")
password2 = input("Enter the password again: ")

if password1 != password2:
    print("Error: Passwords do not match")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters long")
elif password1 in BAD_PASSWORDS:
    print("Error: Password is too common. Choose a different one.")
else:
    print("Password Set")