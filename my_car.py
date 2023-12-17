# Assume you have a file named 'my_module.py' with the following content:

# my_module.py
class MyClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("My name is", self.name)

# Now, let's import the MyClass from my_module.py in another file:

# main.py

# Import the MyClass class from my_module.py
from my_module import MyClass

# Create an instance of MyClass
my_instance = MyClass("John")

# Call the display_name method of the MyClass instance
my_instance.display_name()
