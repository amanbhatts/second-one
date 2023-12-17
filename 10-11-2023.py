class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        def move(self):
            print("Move")
class Boat(Vehicle):

    def move(self):
        print("sail")

class Plane(Vehicle):

    def move(self):
        print("fly")

b = Boat("Ibiza", "Tour 20")
p = Plane("boing", "747")

print(b.brand)
print(b.model)
b.move()

print(p.brand)
print(p.model)
p.move()