# Define the filename of the text file containing the digits of pi
filename = 'pi_digits.txt'

# Open the file in read mode using a 'with' statement, which ensures that the file is properly closed after reading
with open(filename) as file_object:
    # Read all the lines from the file and store them in a list called 'lines'
    lines = file_object.readlines()

# Initialize an empty string to store the digits of pi
pi_string = ''

# Iterate through each line in the list of lines
for line in lines:
    # Strip any trailing whitespaces (like newline characters) from each line and append it to the 'pi_string'
    pi_string += line.rstrip()

# Print the concatenated string of pi digits
print(pi_string)

# Print the total number of characters (digits) in the pi string
print(len(pi_string))