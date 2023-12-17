file_path = 'E:\Cashback (2006) [BluRay] [1080p] [YTS.AM]\Alice in wonderland.txt'
file_name = "Alice in Wonderland"
try:
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry the {file_name} does not exist")
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {file_name} has about {num_words} words.")