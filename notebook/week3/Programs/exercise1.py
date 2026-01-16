# Exercise 1: Modified greeting program
print("=== Exercise 1: Greeting Program ===")
name = input("Please enter your name: ")

if name.strip() == "":
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}!")


