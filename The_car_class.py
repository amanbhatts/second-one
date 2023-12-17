# Define a class named Car
class Car:
    """A simple attempt to describe a car."""

    # Constructor (__init__) method to initialize attributes
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        # Instance variables or attributes
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23  # Default odometer reading set to 23 miles

    # Method to get a neatly formatted descriptive name of the car
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # Method to print the car's mileage
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Method to update the odometer value
    def update_odometer(self, mileage):
        """Set the odometer value to a given value.
        Rejects the change if it attempts to roll back the value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    # Method to increment the odometer reading by a given amount
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# Create an instance of the Car class
my_used_car = Car('audi', 'a4', 2019)

# Print the descriptive name of the car
print(my_used_car.get_descriptive_name())

# Update the odometer reading to 23,500 miles and print the mileage
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# Increment the odometer reading by 100 miles and print the updated mileage
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
