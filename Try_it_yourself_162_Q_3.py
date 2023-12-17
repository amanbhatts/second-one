class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"E-mail: {self.email}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name} who is {self.age} year old.")


# Creating Instances.
user_1 = User("aman", "bhatt", "30", "Bareilly", "abcdefg@gmail.com")
user_2 = User("ketan", "bhatt", "28", "Bareilly", "ablufh@gmail.com")

# calling instances!!
user_1.greet_user()
user_1.describe_user()
user_2.greet_user()
user_2.describe_user()