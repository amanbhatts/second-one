"""Assignment 5
Create a python class with the below attributes and access the same via an object

The class ‘Phone’ would have certain properties associated with such as:

Color
Cost &
Battery Life
Similarly, the class ‘Phone’ would have certain behavior associated with such as:

You can make a call
You can watch videos &
You can play games"""

class Phone:
    def __init__(self, color, cost, battery_life):
        self.color = color
        self.cost = cost
        self.battery_life = battery_life

    def make_a_call(self):
        print("making a call")

    def watch_videos(self):
        print("watching videos")

    def play_games(self):
        print("play games")

# creating instances
phone_1 = Phone("Red", "99$", "20 Hours")
phone_2 = Phone("Black", "109$", "28 Hours")

# accessing attributes
print(f"The color of phone: {phone_1.color}| Cost of phone: {phone_1.cost}| Battery life: {phone_1.battery_life}")
print(f"\nThe color of phone: {phone_2.color}| Cost of phone: {phone_2.cost}| Battery life: {phone_2.battery_life}\n")

# calling instances
phone_1.make_a_call()
phone_1.play_games()
phone_1.watch_videos()

print("\n")

phone_2.make_a_call()
phone_2.watch_videos()
phone_2.play_games()