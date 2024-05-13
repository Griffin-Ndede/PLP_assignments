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

class A():
    def __init__(self,count=100):
        self.count=count
obj1=A()
obj2=A(102)

print(obj1.count)
print(obj2.count)