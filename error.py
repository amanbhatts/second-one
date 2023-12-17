try:
    print(x)
except NameError:
    print("Variable X is not defined")
except:
    print("Something went wrong")

# else used to define a block of code to be executed if no error were raised
try:
    print("Hello")
except:
    print("something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("close the browser")

# custom exceptio0ns - define the exceptions based on the requirementusing raise
# keyword if the condition occurs

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero are allowed")