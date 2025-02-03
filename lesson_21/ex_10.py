# Class Exercise:
# Create a Python class representing a car with methods for accelerating and braking.

class Car:
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5
        print(f"The {self.make} {self.model} is accelerating. Current speed: {self.speed} km/h")

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
            print(f"The {self.make} {self.model} is braking. Current speed: {self.speed} km/h")
        else:
            self.speed = 0
            print(f"The {self.make} {self.model} has stopped. Current speed: {self.speed} km/h")

    def get_speed(self):
        return self.speed

my_car = Car("Toyota", "Camry", 2020)

my_car.accelerate()
my_car.accelerate()
my_car.brake()
my_car.brake()
my_car.brake()
