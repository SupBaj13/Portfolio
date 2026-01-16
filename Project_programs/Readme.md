# Introduction to Programming – Final Assignment
This repository provides Python solutions for Task 1 and Task 2 of the final assignment, highlighting input validation, conditional statements, loops, and basic computational logic.
# Task 1: Beckett Pizza Plaza 4-for-3 Offer

Description
This script implements BPP's 4-for-3 promotion. Customers order exactly four pizzas; the cheapest is free. The program validates inputs, excludes the lowest price, calculates the total, and displays the discount percentage.

## Rules Applied
-Prices must be positive numbers (>0)

-Invalid non-numeric inputs rejected

-Discount = (cheapest/sum of all) × 100%, max 25%

-Exactly four pizzas required

## Key Learnings:
-Loop for exactly four valid inputs

-Store prices in lists

-Input validation with try/except

-Transform business rules into structured code


# Task 2: Password Security Checker
Description
This script validates a password by checking its length (>=9 characters) and then quizzes the user on three random character positions. The program exits immediately if length is insufficient or any position is answered incorrectly.

## Rules Applied
-Password must be 9+ characters long

-Three random 1-indexed positions requested

-Exact character match required at each position

-Same position may be asked multiple times

-Failure at any check terminates program


## Key learnings:
-String indexing with 1-based user positions (password[pos-1])

-random.randint() for position selection

-Loop control with early break on failure

-Input validation without try/except needed

-Clear success/failure messaging patterns
## Technologies used:
-Vs code
-Python3

