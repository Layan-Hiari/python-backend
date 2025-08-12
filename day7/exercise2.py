class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed}. Species: {self.species}."

dog1 = Dog("Vega", "Basenji")
dog2 = Dog("Roux", "Saluki")

print(dog1.describe())
print(dog2.describe())

dog2.species = "Canis lupus"

print(dog1.describe())
print(dog2.describe())
