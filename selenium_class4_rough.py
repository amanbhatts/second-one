name = "Alice"
age = 30
formatted_string = f"hello My name is Alice and i am {age} years old"
print(formatted_string)


name = "Alice"
age = 30
formatted_string = f"Hello, {name}! You are {age} years old."
print(formatted_string)


quantity = 3
item_no = 658
price = 78.90
formatted_string = "I want pay {} dollars for {}"
print(formatted_string.format(quantity,item_no,price))


# check if the item exist
this_list = ["apple", "guava", "banana", "cherry"]
if "apple" in this_list:
    print("yes the item is in the list")
if "banana" not in this_list:
    print("No, the item is not in this list")
else:
    print("item is present")

# using for loops
this_list = ["apple", "guava", "banana", "cherry"]
for i in this_list:
    print(i)

# range() and len()
this_list = ["apple", "guava", "banana", "cherry"]
for x in range(len(this_list)):
    print(this_list[x])

# sorting - alphanumeric and ascending default
this_list = ["apple", "guava", "banana", "cherry"]
this_list.sort()
print(this_list)

# copy method

# copy
this_list = ["apple", "guava", "banana", "cherry"]
mylist = this_list.copy()
print(mylist)

# join()
list1 = ["banana", "orange", "cherry"]
list2 = ["pomo", "apple"]
list3 = list1 + list2
print(list3)

this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print(this_tuple[1])
print(this_tuple[1:2])

# loop tuple
this_tuple = ("apple", "guava", "banana", "cherry")
for x in range(len(this_tuple)):
    print(this_tuple[x])

# joining tuple
tuple1 =("kiwi", "tomato", "pumpkin")
tuple2 =("klkl", "jhjh", "tyty")
tuple = tuple1 + tuple2
print(tuple)


this_tuple = ("apple", "guava", "banana", "cherry")
list1 = list(this_tuple)
list1[1] = "kiwi"
new_tuple = tuple(list1)
print(newtuple)
