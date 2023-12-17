# Explanation of Lists:
# - Lists are a versatile and mutable data type in Python.
# - They are ordered, meaning the elements have a specific order.
# - Lists can contain elements of different data types, such as integers, strings, or other lists.
# - Elements in a list are indexed, starting from 0 for the first element.
# - Lists can be modified after creation, allowing for dynamic changes to the data they hold.

# Code Example:

# Creating a list
my_list = [1, 2, 3, "apple", "orange", [4, 5]]

# Displaying the original list
print("Original List:")
print(my_list)

# Adding elements to the list
my_list.append("banana")  # Adds "banana" to the end of the list
my_list.insert(2, "grape")  # Inserts "grape" at index 2

# Displaying the list after adding elements
print("\nList after adding elements:")
print(my_list)

# Modifying elements in the list
my_list[0] = 10  # Changes the element at index 0 to 10
my_list[3] = "cherry"  # Changes the element at index 3 to "cherry"

# Displaying the list after modifying elements
print("\nList after modifying elements:")
print(my_list)

# Removing elements from the list
removed_element = my_list.pop()  # Removes and returns the last element
del my_list[1]  # Removes the element at index 1

# Displaying the list after removing elements
print("\nList after removing elements:")
print(my_list)

# Displaying the removed element
print("\nRemoved Element:", removed_element)
