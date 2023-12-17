class Vehicle:
    def drive(self):
        print("Driving a vehicle")

class Car(Vehicle):
    def drive(self):
        print("Repairing a car")


my_car = Car()


my_car.drive()