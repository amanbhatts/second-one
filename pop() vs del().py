# Creating a list
my_list = [1, 2, 3, 4, 5]

# Displaying the original list
print("Original List:", my_list)

# Using pop without index (removes and returns the last element)
popped_element = my_list.pop()
print("\nAfter pop without index:")
print("List:", my_list)
print("Popped Element:", popped_element)

# Using pop with index (removes and returns the element at index 1)
popped_element_at_index = my_list.pop(1)
print("\nAfter pop at index 1:")
print("List:", my_list)
print("Popped Element at index 1:", popped_element_at_index)

# Using del with index (removes the element at index 2)
del my_list[2]
print("\nAfter del at index 2:")
print("List:", my_list)

# Using del with slice (removes elements from index 1 to 3)
del my_list[1:4]
print("\nAfter del with slice:")
print("List:", my_list)

# ---------output----------

"""Original List: [1, 2, 3, 4, 5]

After pop without index:
List: [1, 2, 3, 4]
Popped Element: 5

After pop at index 1:
List: [1, 3, 4]
Popped Element at index 1: 2

After del at index 2:
List: [1, 3]

After del with slice:
List: [1]"""