bicycles = ['trek', 'canondale', 'redline', 'giant']
print(bicycles)
# it will just print the above list as it is with all the commas and square bracket

# but we dont want this, we want our output list items to be clean. So we use access the list
print(bicycles[0]) # zero is the index of first element
# it will print first element as output i.e trek.

# we can also use .title() , .upper(), .lower() etc with out output list
print(bicycles[1].upper())
print(bicycles[2].title())

# we can also access LAST elements using negetive indexing.
print(bicycles[-4]) # remember that here negetive indexing starts from -1 not 0.

#Using individual values from the list
message = "my first bicycle was {} ".format(bicycles[0].title())
print(message)

# remove item using remove().
bike = ['trek', 'canondale', 'redline', 'giant']
print(bike)
bike.remove('canondale')
print(bike)
print(bike.sort())
bike.sort(reverse = True)

print(bike)



