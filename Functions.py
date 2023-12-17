def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Calling the function with three name parts
musician = get_formatted_name('john', 'hooker')
print(musician)

# Calling the function with two name parts (no middle name)
musician = get_formatted_name('aman','bhatt')
print(musician)