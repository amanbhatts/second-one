# Assume you have a file named 'my_module.py' with the following content:

# my_module.py
class MyClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("My name is", self.name)

# Now, let's import the MyClass from my_module.py in another file:

# main.py

# Import the MyClass class from my_module.py with an alias 'MyAlias'
from my_module import MyClass as MyAlias

# Create an instance of MyClass using the alias
my_instance = MyAlias("John")

# Call the display_name method of the MyClass instance using the alias
my_instance.display_name()

# Benefits of using aliases:

# 1. **Shortening Names:**
#    Aliases can be used to provide shorter and more convenient names, especially for modules or classes with long names.

# 2. **Avoiding Naming Conflicts:**
#    If there is a potential for naming conflicts (e.g., if there are multiple modules with similar names), aliases can help differentiate between them.

# 3. **Code Readability:**
#    Aliases can improve code readability by providing more meaningful or descriptive names in the context of the current code.

# 4. **Renaming without Impact:**
#    If you need to rename a module or a class, using aliases allows you to update the import statement in one place without changing the rest of the code.

# Example of benefits:

# Without alias:
# from my_module_with_a_very_long_name import SomeClassWithAVeryLongName

# With alias:
# from my_module_with_a_very_long_name import SomeClassWithAVeryLongName as ShortAlias
