favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']

for name in set(sorted(favorite_language.values())):
    print(f"{name.title()} thank you for your poll.")

