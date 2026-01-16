# Exercise 7: Custom Times Table
print("\n=== Exercise 7: Custom Times Table ===")
try:
    table_number = int(input("Enter a number between 0 and 12: "))
    
    if table_number < 0 or table_number > 12:
        print("Error: Number must be between 0 and 12 inclusive")
    else:
        for i in range(13):
            result = i * table_number
            print(f"{i} x {table_number} = {result}")
except ValueError:
    print("Error: Please enter a valid number")