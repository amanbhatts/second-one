def add_numbers():
    try:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 + num2

        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter the numerical values.")

add_numbers()
