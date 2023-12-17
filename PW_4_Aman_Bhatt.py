"""1. Print First 10 natural numbers using while loop
2. Calculate the sum of all numbers from 1 to a given number
3.Write a program to print multiplication table of a given number - 2
4.write a program to print first 10 odd numbers
5.Write a program to find the factorial of a number"""

# print first 10 natural numbers using loop.
for i in range(1 ,11):
    print(i)

# calculate the sum of all numbers from 1 to a given number.
num = int(input("Enter a number: "))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1      # as we use i++ in C++.
print("Sum of numbers from 1 to", num, "is:", sum)


# Write a table of 2.
num = 3
print("Multiplication table for", num)
for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)

# Write a program to print first 10 odd numbers.
count = 0
num = 1

print("First 10 odd numbers:")
while count < 10:
    if num % 2 != 0:
        print(num)
        count += 1
    num += 1

# Write a program to find a factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
factorial_result = factorial(num)
print("Factorial of", num, "is:", factorial_result)