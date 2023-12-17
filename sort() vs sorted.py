# Creating a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Using sort() method (in-place sorting)
my_list.sort()
# sort() modifies the original list in-place and returns None
# The sorted list is now stored in my_list
print("List after sort() method:", my_list)

# Creating a new list
another_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Using sorted() function (returns a new sorted list)
sorted_another_list = sorted(another_list)
# sorted() creates a new sorted list and leaves the original list unchanged
print("Original List:", another_list)
print("New List after sorted() function:", sorted_another_list)

# ------Output------
"""List after sort() method: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
Original List: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
New List after sorted() function: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
"""