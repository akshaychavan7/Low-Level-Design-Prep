class Car:
    def __init__(self):
        self.engine = None
        self.color = None
    
    def __str__(self):
        return f"{self.color} car with {self.engine} engine"

class CarBuilder:
    def __init__(self):
        self.car = Car()
    
    def setEngine(self, engine):
        self.car.engine = engine
        return self

    def setColor(self, color):
        self.car.color = color
        return self
    
    def build(self):
        return self.car

car = CarBuilder().setColor("Red").setEngine("V8").build()
print(car)

"""
Builder Design Pattern is used to construct complex objects step-by-step in a flexible and readable way.
📌 Why Use the Builder Pattern?
    - Useful when you have many optional fields or complex construction logic.
    - Avoids telescoping constructors (multiple overloaded constructors).
    - Makes code more readable and maintainable.
"""