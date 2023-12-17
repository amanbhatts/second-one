quantity = 23
item_no = 48
price = 567
print("We need", quantity, "articles of item number", item_no,"for", price, "Dollar")

my_order = "We need {} articles of item number {} for {} Dollar"
print(my_order.format(quantity, item_no, price))


this_list = ["apple", "banana", "cherry", "765"]
print(this_list)
print(len(this_list))
print(type(this_list))
print(this_list[1])

this_list[1] = "kiwi"
print(this_list)
this_list[:2] = ["tomato", "papaya", "dragon_fruit"]
print(this_list)

# insert elements
this_list.append("orange")
print(this_list)
this_list.insert(3, "Grape")
print(this_list)

# remove elements

this_list.remove("papaya")
print(this_list)

# del remove at specific index
del this_list[2]
print(this_list)

# pop remove
this_list.pop(2)
print(this_list)
