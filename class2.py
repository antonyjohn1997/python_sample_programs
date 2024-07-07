class Animal:
    def __init__(self, name, age):
        self._name = name    # Protected attribute
        self._age = age      # Protected attribute

    def _display_info(self):  # Protected method
        print(f"Name: {self._name}, Age: {self._age}")

    def public_method(self):
        print("This is a public method.")
        self._display_info()  # Calling protected method within the class

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed  # Protected attribute

    def display_breed(self):
        print(f"Breed: {self._breed}")
        self._display_info()  # Accessing protected method from subclass

# Creating an instance of Dog
dog = Dog("Buddy", 3, "Golden Retriever")

# Accessing public method
dog.public_method()  # Output: This is a public method. Name: Buddy, Age: 3

# Accessing protected attribute and method from outside (not recommended)
print(dog._name)  # Output: Buddy
dog._display_info()  # Output: Name: Buddy, Age: 3

# Accessing protected method from subclass
dog.display_breed()  # Output: Breed: Golden Retriever, Name: Buddy, Age: 3
