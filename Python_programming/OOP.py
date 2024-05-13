# class Person:
#     def __init__(self, name="Griffin", age=20, nationality="Kenyan"):
#         self.name = name
#         self.age = age
#         self.nationality = nationality
#     def displayInfo(self):
#         print("Person name:",self.name, "Person age:", self.age, "Nationality", self.nationality)

# del Person

# p1 = Person("Griffin", "Kenyan", 30)
# print(p1.displayInfo())


# class Person:
#     def person_info(self, name, age):
#         print('Name', name, "age", age, "Inside Person class")

# class Company:
#     def company_info(self, company_name, location):
#         print("Name", company_name, "location", location)

# class Employee(Person, Company):
#     def employee_info(self, salary, skill):
#         c_name = super().company_info()
#         print("Salary", salary, "Skill", skill, c_name)

# emp =Employee()
# emp.person_info("Griffin", 30)
# emp.company_info("Little", "Westlands")
# emp.employee_info(15000, "Intern")

# # print(emp)
# # print (emp.company_info())


# class Student:
#     schoolName = "PLP Academy"

#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

# std = Student("Griffin", 25)
# std.age = 30
# std.name = "Ian"
# print(std.schoolName, std.__name, std.age)

# class A():
#     def __init__(self,count=100):
#         self.count=count
# obj1=A()
# obj2=A(102)

# print(obj1.count)
# print(obj2.count)

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationYear = year
    
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationYear)
# #Use the Person class to create an object, and then execute the printname method:
# x = Student("Griffin", "Omondi", 2022)
# x.welcome()

def age():
    age = int(input("How old are you?:"))
    if age >= 18:
        print (f"You are old enough to be drinking alcohol since you are {age} years old")
    else:
        print("You should not be anywhere near alcohol")

print(age())
