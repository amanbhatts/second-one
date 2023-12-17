this_tuple = ("apple", "guava", "banana", "cherry")
list1 = list(this_tuple)
list1[1] = "kiwi"
new_tuple = tuple(list1)
print(new_tuple)

# add item to tuple
this_tuple = ("apple", "guava", "banana", "cherry")
list1 = list(this_tuple)
list1.append("momo")
new_tuple = tuple(list1)
print(new_tuple)

# unpacking - allow to extract the values back into the variables
this_tuple = ("apple", "guava", "banana", "cherry")
(a,b,c,d) = this_tuple
print(a)
print(b)
print(c)
print(d)