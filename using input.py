# Demonstrate the use of input() function
name = input("Enter your name: ")  # Prompt the user to enter their name
print("Hello, " + name + "!")

# Demonstrate += with input()
age = input("Enter your age: ")  # Prompt the user to enter their age
age = int(age)  # Convert the input (which is a string) to an integer using int()
age += 5  # Increment the age by 5 using +=
print("In 5 years, you will be", age, "years old.")

# Demonstrate the modulo operator (%)
number = int(input("Enter a number: "))  # Prompt the user to enter a number and convert it to an integer
remainder = number % 2  # Use the modulo operator to check if the number is even or odd
if remainder == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

