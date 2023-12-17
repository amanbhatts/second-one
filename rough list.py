# Explanation of reverse() and len():
# - reverse() is a method that reverses the elements of a list in-place.
# - len() is a built-in function that returns the number of items in an object, such as a list.

# Program using reverse() and len():

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Displaying the original list
print("Original List:", my_list)

# Using reverse() method (reverses the list in-place)
my_list.reverse()
# The list is now reversed in-place
print("List after reverse():", my_list)

# Using len() function to get the length of the list
list_length = len(my_list)
# len() returns the number of items in the list
print("Length of the List:", list_length)

"""
Original List: [1, 2, 3, 4, 5]
List after reverse(): [5, 4, 3, 2, 1]
Length of the List: 5
"""
