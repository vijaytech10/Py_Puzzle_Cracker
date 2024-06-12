"""
1. Create a Car class and Create 2 Objects of the
class with attributes 5 and 5 methods

2. Create a Class Person, Two Objects by taking
(name, age, address) Input from users and print
details in the end.

"""
class car():

    def __init__(self, brand, fuel):
        self.brand = brand
        # self.colour = colour
        self.fuel = fuel
        # self.fuel = fuel
        # self.year = year

    def engine(self):
        print ("Petrol Engine" + " " + self.brand + " -" + self.fuel)

    def start(self):
        print ("insert car keys" + self.brand + self.fuel)

    def move(self):
        print("Enable gear & move" + self.brand + self.fuel)

swift = car()
micra = car()
nexon = car()

swift.brand = "suzuki"
# swift.type = "vxi"
# micra.colour = "blue"
nexon.fuel = "battery"

swift.engine(swift)

