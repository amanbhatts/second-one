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

# Define a subclass named ElectricCar that inherits from Car
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""


    def __init__(self, make, model, year):
        """Initialize attributes of the parent class,
        then initialize attributes specific to an electric Car."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

# Create an instance of ElectricCar called my_tesla
my_tesla = ElectricCar('tesla', 'model s', 2019)

# Print a descriptive name for the ElectricCar instance
print(my_tesla.get_descriptive_name())

# Call the describe_battery method to print information about the battery size
my_tesla.describe_battery()
