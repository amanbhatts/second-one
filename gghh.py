class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine speciality is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open")

# Creating instances!!
restaurant_1 = Restaurant("Santa Banta", "Chinese")
restaurant_2 = Restaurant("Punjabi Tadka", "Punjabi")
restaurant_3 = Restaurant("Al Nawaz", "Muglai")

# Calling Instances!!
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


