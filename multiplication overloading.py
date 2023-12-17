class Multiplication:
    """Multiplication for overloading in 28-11-2023"""
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def multiply(self):
        return self.var1 * self.var2

class Multiplication3(Multiplication):
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2)
        self.var3 = var3

    def multiply(self):

        return self.var1 * self.var2 * self.var3


multiplier2 = Multiplication(3, 4)
result2 = multiplier2.multiply()
print(f"Multiplication result for two variables: {result2}")

multiplier3 = Multiplication3(2, 5, 7)
result3 = multiplier3.multiply()
print(f"Multiplication result for three variables: {result3}")