# Exercise 3: Password with length check

print("\n=== Exercise 3: Password with Length Check ===")
password1 = input("Enter a new password (8-12 characters): ")
password2 = input("Enter the password again: ")

if password1 != password2:
    print("Error: Passwords do not match")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters long")
else:
    print("Password Set")