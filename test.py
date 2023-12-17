"""
1. The sum of the first five positive integers
2.The average age of Sara (age 23), Mark (age 19), and Fatima (age 31)
3. The number of times 73 goes into 403
4.The remainder when 518 is divided by 73
5.The lowest price among the following prices:  34.99,29.95, and $31.50
6.The sum of 2 and 2 is less than 4.
7.The value of 7 // 3 is equal to 1 +
8.The sum of 2, 4, and 6 is greater than 12.
9.1387 is divisible by 19.
10.31 is even.
11.Write Python expressions using s1, s2, and s3 and operator +
(a) 'ant bat cod'
"""
# Sum of the first five positive integer
n = 5
sum_of_first_five_integers = n * (n+1) / 2
print("The sum of first 5 integers is", sum_of_first_five_integers)

# The average age of Sara (age 23), Mark (age 19), and Fatima (age 31).

sara = 23
mark = 19
fatima = 31
average_age = (sara + mark + fatima) / 3
print("the average age of Sara, Mark and Fatima is:", average_age)

# The number of times 73 goes into 403.
remainder = 403 // 73
print("73 goes into 403:", remainder, "times")

# The remainder when 518 is divided by 73
remainder = 518 % 73
print("The remainder when 518 is divided by 73 is:", remainder)

# The lowest price among the following prices: 34.99, 29.95, and 31.50.
price_1st = 34.99
price_2nd = 29.95
price_3rd = 31.50
lowest_price = min(price_3rd, price_2nd, price_1st)
print("The lowest price is:", lowest_price)

# The sum of 2 and 2 is less than 4.
answer = 2 + 2 < 4
print("Is 2 + 2 less than 4:", answer)

# The value of 7 // 3 is equal to 1 + 1.
value = 7 // 3 == 1 + 1
print("is the value 7 // 3 = 1 + 1 :", value)

# The sum of 2, 4, and 6 is greater than 12.
sum = 2 + 4 + 6 > 12
print("is the sum of 2, 4 and 6 greater than 12?", sum)

# 1387 is divisible by 19.
result = 1387 % 19 == 0
print("is 1387 divisible by 19:", result)

# 31 is even.
result = 31 % 2 == 0
print("Is 31 an Even number:", result)

# Write Python expressions using s1, s2, and s3 and operator +
# (a) 'ant bat cod'
s1 = "'ant"
s2 = "bat"
s3 = "cod'"
result = s1 + ' ' + s2 + ' ' + s3
print("After Concatenation:", result)