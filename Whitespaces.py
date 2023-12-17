# to add tab to your text use \t

print("python")
print("\tpython")

#|python|
#|  python|


# To add a new line into the string use the character combination \n:

print("Languages:\nPython\nJava\nC++")

#|Languages:
#Python
#Java
#C++|


# Original string with trailing spaces
message = "  Hi, I am trying to use rstrip   "

# Removing trailing spaces using rstrip()
stripped_message = message.strip()

# Output before and after using rstrip()
print("Original Message:", repr(message))  # repr() is used to show whitespace characters
print("Stripped Message:", repr(stripped_message))
message = "  Hello   "
print(repr(message))

message = message.rstrip()
print(repr(message))
print(0.2 + 0.3)