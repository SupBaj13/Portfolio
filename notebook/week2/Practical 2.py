"""
Introduction to Programming - Week 2 Lab Worksheet Solutions
This file contains solutions to all the tasks in the Week 2 lab worksheet.
"""

print("=== TASK: Working with Variables ===")
print("\n--- Task 1: Basic variable usage ---")
total = 100
print("The total is", total)

print("\n--- Task 2: Variable reassignment ---")
total = total + 99
print("The total is now", total)

print("\n--- Task 3: Augmented assignment ---")
total = 100  # Reset total
total += 99
print("The total is now", total)

print("\n--- Task 4: More augmented assignment practice ---")
total = 100  # Reset total
total -= 1
print("The total is", total)

total *= 4
print("The total is", total)

total /= 2
print("The total is", total)

print("\n--- Task 5: Calculate average ---")
total = 98.2
count = 5
average = total / count
print("The average is:", average)

print("\n=== TASK: Data-Types ===")
print("\n--- Task 1: Using type() function ---")
print("Type of False:", type(False))
print("Type of 1000:", type(1000))
print("Type of 100.111:", type(100.111))
print("Type of 'Hello':", type("Hello"))
print("Type of True:", type(True))
print("Type of 100 / 5:", type(100 / 5))
print("Type of 100 // 5:", type(100 // 5))

print("\n--- Task 2: String operations ---")
print("Result of 'ABC' * 10:", "ABC" * 10)
print("The * operator repeats the string the specified number of times.")

print("\n=== TASK: Calling Built-in functions ===")
print("\n--- Task 1: Display personal information ---")
name = "John Smith"
address = "123 Main Street, Leeds"
contact = "john.smith@example.com"
print("Name:", name)
print("Address:", address)
print("Contact:", contact)
print("Length of name:", len(name))

print("\n--- Task 2: User input with error ---")
# Uncomment to test (commented to avoid interrupting the program flow)
# age = input("Enter your age ")
# print("in one year your age will be", age + 1)  # This will cause an error

print("\n--- Task 3: User input with conversion ---")
# Uncomment to test
# age = input("Enter your age ")
# age = int(age)
# print("in one year you will be", age + 1)

print("\n--- Task 4: Calculate product of two numbers ---")
# Uncomment to test
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# product = num1 * num2
# print("The product is:", product)

print("\n=== TASK: Single, Double and Triple Quotes ===")
print("\n--- Task 1: Quotes within strings ---")
comment = 'I would have "thought" you knew better!'
print("Using single quotes:", comment)

# Using double quotes (this will cause an error if uncommented):
# comment = "I would have "thought" you knew better!"  # Syntax error

print("\n--- Task 2: Using escape sequences ---")
print("This text includes characters such as '\\' '\"' and \"'\",")
print("This is a new line that starts with a tab")
print("This new line starts with two tabs")

print("\n--- Task 3: Display backslashes ---")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("Hello there!")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

print("\n--- Task 4: Using triple quotes ---")
print("""This text spans three lines,
and includes both single ('),
and double quotes (").""")

print("\n=== TASK: Indexing and Slicing ===")
print("\n--- Task 1: Basic indexing ---")
surname = "Palin"
initial = surname[0]
print("First character:", initial)

print("\n--- Task 2: Access third character ---")
third_char = surname[2]
print("Third character:", third_char)

print("\n--- Task 3: Access out-of-range index ---")
# This will cause an error if uncommented:
# tenth_char = surname[9]  # IndexError: string index out of range

print("\n--- Task 4: Negative indexing ---")
last = surname[-1]
print("Last character:", last)

print("\n--- Task 5: Second from last character ---")
second_last = surname[-2]
print("Second from last character:", second_last)

print("\n--- Task 6: Slicing ---")
surname = "Palin"
middle = surname[1:4]
print("Characters 1 to 4:", middle)

print("\n--- Task 7: Slice all except first character ---")
tail = surname[1:]
print("All characters except first:", tail)

print("\n--- Task 8: Slice all except last character ---")
all_except_last = surname[:-1]
print("All characters except last:", all_except_last)

print("\n--- Task 9: Negative slicing ---")
last_three = surname[-3:]
print("Last three characters:", last_three)

print("\n=== TASK: Introducing Lists ===")
print("\n--- Task 1: List creation and slicing ---")
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
first_four = primes[:4]
print("First four prime numbers:", first_four)

print("\n--- Task 2: List mutation ---")
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
print("Original list:", names)

# Replace first element
names[0] = "Terry, G."
print("After replacing first element:", names)

# Insert three names at the beginning
names[0:0] = ["Tim", "Bill", "Graeme"]
print("After inserting at beginning:", names)

print("\n--- Task 3: Insert before final name ---")
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]  # Reset
names[-1:-1] = ["Brian", "Neil"]  # Insert before the last element
print("After inserting before final name:", names)

print("\n--- Task 4: List concatenation ---")
names = ["Terry", "John", "Michael"]
names = names + ["Mark"]  # Creates a new list
print("After concatenation:", names)

names += ["Jacob"]  # Mutates the existing list
print("After augmented assignment:", names)

print("\n--- Task 5: List multiplication ---")
nums = [1, 2, 3] * 5
print("Result of [1,2,3] * 5:", nums)
print("The list [1,2,3] is repeated 5 times to create:", nums)

print("\n=== Key Terminology ===")
print("""
● Assignment: The process of storing a value in a variable using the = operator
● Data-type: The classification of data which tells the compiler/interpreter how to use the data
● Argument: A value passed to a function when it is called
● Indexing: Accessing individual elements in a sequence using their position
● Slicing: Accessing a range of elements from a sequence using start and end positions
● Mutable: Data types that can be changed after creation (e.g., lists)
● Immutable: Data types that cannot be changed after creation (e.g., strings, tuples)
""")

print("\n=== All tasks completed! ===")