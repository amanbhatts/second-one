# Open the guest_book.txt file in append mode
with open('guest_book.txt', 'a') as guest_book:
    # Use a while loop to continuously prompt the user for their name
    while True:
        # Prompt the user to enter their name
        name = input("Enter your name (type 'exit' to end): ")

        # Check if the user wants to exit
        if name.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'

        # Greet the user
        print(f"Hello, {name.title()}! Welcome!")

        # Record the visit in the guest_book.txt file
        guest_book.write(f"{name.title()}'s visit\n")

# Print a message indicating the program has ended
print("Thank you for using the guest book!")
#This program prompts the user to enter their name, greets them, and
# records their visit in a file called guest_book.txt. It continues this
# process until the user types "exit." The name is formatted using title()
# to ensure consistent capitalization. The program ends with a message thanking
# the user for using the guest book. The with open('guest_book.txt', 'a') as
# guest_book: line ensures that the file is properly closed after writing.
# The '\n' in the write function ensures that each entry appears on a new
# line in the file.

