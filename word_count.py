def count_words(file_name):
    """Count the approximate number of words in a file"""
    try:
        with open(file_name, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The {file_name} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")

file_names = ['Alice in wonderland.txt', 'Moby_Dick.txt']
for file_name in file_names:
    count_words(file_name)