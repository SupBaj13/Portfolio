
# Exercise 8: Custom Times Table with reverse option
print("\n=== Exercise 8: Times Table with Reverse Option ===")
try:
    table_number = int(input("Enter a number (negative for reverse table): "))
    
    if table_number < -12 or table_number > 12:
        print("Error: Number must be between -12 and 12 inclusive")
    else:
        if table_number >= 0:
            for i in range(13):
                result = i * table_number
                print(f"{i} x {table_number} = {result}")
        else:
            for i in range(12, -1, -1):
                result = i * abs(table_number)
                print(f"{i} x {abs(table_number)} = {result}")
except ValueError:
    print("Error: Please enter a valid number")