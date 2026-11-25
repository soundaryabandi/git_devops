# Parent class
class Person:
   def __init__(self, name, id):
       self.name = name
       self.id = id
   def display(self):
       print(self.name, self.id)
# Child class
class Employee(Person):
   def print_emp(self):
       print("Employee class called")
# Creating an instance of the Employee class
emp = Employee("John", 101)
emp.display() # Output: John 101
emp.print_emp() # Output: Employee class called