import random

password = input("Enter your password: ")
if len(password) < 9:
    print("Password too short.")
else:
    passed = True
    for i in range(3):
        pos = random.randint(1, len(password))
        char = input(f"Enter letter at position {pos}: ")
        if char != password[pos - 1]:
            print("Security check failed.")
            passed = False
            break
        print("Correct")
    if passed:
        print("Security check passed.")
