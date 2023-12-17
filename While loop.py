# In programming, a flag is a boolean variable that signals when a certain condition has been met.
# Flags are commonly used to control the flow of a program, especially in loops.

# Set up the initial prompt for the user
prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to exit the program: "

# Initialize the flag 'active' to True
active = True

# Start a loop controlled by the 'active' flag
while active:
    # Prompt the user to enter a message
    message = input(prompt)

    # Check if the entered message is 'quit'
    if message == 'quit':
        # If 'quit' is entered, set the 'active' flag to False
        active = False
    else:
        # If a message other than 'quit' is entered, print the message
        print(message)

# Print a farewell message once the loop is exited
print("Goodbye!")
