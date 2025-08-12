class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person_a = Person("noor", 17)
person_b = Person("Muna", 24)

print(person_a.introduce())
print(person_b.introduce())
