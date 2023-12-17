class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine speciality is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant{self.restaurant_name} is open")

# Creating Instance for restaurant.
restaurant = Restaurant("Santa Banta", "chinese")

# Printing the attributes individually.
print(f"The name of the restaurant is {restaurant.restaurant_name}")
print(f"The cuisine speciality is {restaurant.cuisine_type}")

