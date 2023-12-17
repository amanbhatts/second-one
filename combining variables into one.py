# Combining two variables into one.
# To insert a variables value into a string, place the letter f
# immediately before the opening quotation mark.

first_name = "Ada"
second_name = "Lovelace"
full_name = f"{first_name} {second_name}"
print(full_name)

# Output will be |Ada Lovelace|


message = f"Hello,{full_name.title()}!"
print(message


# |Hello, Ada Lovelace!|

