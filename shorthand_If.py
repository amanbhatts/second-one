a = 330
b = 330
print("A") if a > b else print("B")
print("Both are equal") if a.__eq__(b) else print("Upper one is true")

a = 200
b = 33
c = 500
if a > b and c > a:
    print ("Both conditions are true")

if a > b or a > c:
    print("At least one of the conditions is True")

if not a > b:
    print("a is NOT greater than b")
