class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def displayInfo(self):
        print("Person name:",self.name, "Person age:", self.age, "Nationality", self.nationality)
p1 = Person("Griffin", "Kenyan", 30)

print(p1.displayInfo())