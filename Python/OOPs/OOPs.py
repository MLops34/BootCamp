class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print(self.name + " is starting.")

class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model

    def start(self):
        print(self.color + " " + self.name + " (" + self.model + ") is ready to go.")

class ElectricCar(Car):
    def __init__(self, name, color, model, battery_capacity):
        super().__init__(name, color, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(self.name + " is charging with " + str(self.battery_capacity) + "kWh battery.")

v1 = Vehicle("Bike", "Red")
v1.start()

c1 = Car("Honda", "Blue", "Civic")
c1.start()

e1 = ElectricCar("Tesla", "White", "Model S", 100)
e1.start()
e1.charge()
