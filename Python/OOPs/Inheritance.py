class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def display(self):
        print(f"Vehicle Name: {self.name}, Wheels: {self.wheels}")

class Bike(Vehicle):
    def __init__(self, name, wheels, engine_type):
        super().__init__(name, wheels)
        self.engine_type = engine_type

    def show_details(self):
        self.display()
        print(f"Engine Type: {self.engine_type}")

bike = Bike("Royal Enfield", 2, "Petrol")
bike.show_details()
