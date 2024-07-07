class Animal:
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()
#animal=Animal()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
#print(animal.speak())

def make_sound(a):# a is just parameter,
    print(a.speak())  # Dynamic binding based on object type

# Usage
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
