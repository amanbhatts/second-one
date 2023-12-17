my_set = {"apple", "banana", "cherry"}
print(my_set)
my_set.add("kiwi")
my_set.remove("cherry")
print(my_set)
my_set.add("banana")
print(my_set)
print(my_set)


# Union of sets
set_1 = {"apple", "banana", "kiwi"}
set_2 = {"kiwi", "orange", "pomo"}
set_1.update(set_2)
print(set_1)
new_set = set_1 | set_2
print(new_set)



