x = input("enter the number")
x = int(x)
print(x)

if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20")