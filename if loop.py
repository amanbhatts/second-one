# Program to demonstrate if, if-else, and elif statements

# Get user input for a number
num = int(input("Enter a number: "))

# Example 1: Simple if statement
if num > 0:
    print("Example 1: The number is positive.")
# The if statement checks if the condition (num > 0) is True.
# If True, it executes the indented block of code.

# Example 2: if-else statement
if num % 2 == 0:
    print("Example 2: The number is even.")
else:
    print("Example 2: The number is odd.")
# The if-else statement checks the condition (num % 2 == 0).
# If True, it executes the first block; otherwise, it executes the else block.

# Example 3: elif statement
if num > 0:
    print("Example 3: The number is positive.")
elif num == 0:
    print("Example 3: The number is zero.")
else:
    print("Example 3: The number is negative.")
# The elif statement is used to check additional conditions after the initial if.
# If the first if condition is False, it checks the next condition in elif.
# If none of the conditions is True, it executes the else block.

# Note: The indentation is crucial in Python and defines the blocks of code.
# The colon (:) at the end of each if, elif, else statement and the proper indentation are essential.

-----output-----
# Enter a number: 12
# Example 1: The number is positive.
# Example 2: The number is even.
# Example 3: The number is positive.