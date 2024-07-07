class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age   # Protected attribute
        self.__salary = 50000  # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

    def get_salary(self):
        return self.__salary

# Create an object of the Person class
person = Person("John", 30)

# Access public attribute
print(person.name)  # Output: John

# Access protected attribute (not recommended, but possible)
print(person._age)  # Output: 30

# Access private attribute (not directly accessible)
# print(person.__salary)  # This will raise an AttributeError

# Access private attribute using getter method
print(person.get_salary())  # Output: 50000

# Modify private attribute using setter method
person.set_salary(60000)
print(person.get_salary())  # Output: 60000

# Trying to set a negative salary
person.set_salary(-1000)  # Output: Invalid salary amount

# Display all information using the public method
person.display_info()  # Output: Name: John, Age: 30, Salary: 60000

