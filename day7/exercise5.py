class Car:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    def display_car(self):
        return f"{self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        return Car.total_cars


car_a = Car("Nexo", "X1")
car_b = Car("Zyra", "Q5")

print(car_a.display_car())
print(car_b.display_car())
print(Car.get_total_cars())
