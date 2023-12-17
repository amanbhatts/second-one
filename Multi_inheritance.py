class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model}")

class Ford(Car):
    def specific_feature(self):
        print("This is a Ford-specific feature.")

class Mercedes(Car):
    def specific_feature(self):
        print("This is a Mercedes-specific feature.")

class Ferrari(Car):
    def specific_feature(self):
        print("This is a Ferrari-specific feature.")

ford_car = Ford("Mustang")
mercedes_car = Mercedes("Benz")
ferrari_car = Ferrari("458 Italia")

ford_car.display_info()
ford_car.specific_feature()

mercedes_car.display_info()
mercedes_car.specific_feature()

ferrari_car.display_info()
ferrari_car.specific_feature()
