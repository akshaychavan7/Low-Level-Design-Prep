class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

"""
- Encapsulates the object creation logic.
- Based on the animal_type string, it dynamically returns an instance of the appropriate class (Cat or Dog).
- Keeps the client decoupled from the actual classes it uses.
"""
class AnimalFactory:
    def get_animal(self, animal_type):
        animals = {
            "cat": Cat,
            "dog": Dog,
        }

        return animals.get(animal_type.lower(), None)()

factory = AnimalFactory()
dog = factory.get_animal("dog")
cat = factory.get_animal("cat")
print(dog.speak())
print(cat.speak())

"""
Factory Method Pattern encapsulates object creation logic and provides flexibility for instantiating related objects without specifying their concrete classes in the client code.

Client code doesn’t need to know about the internal instantiation details of Cat or Dog.

This makes the code more maintainable and extensible.

Benefits of Factory Method Pattern
Advantage	Description
Encapsulation	Object creation logic is hidden from the client.
Loose coupling	Client depends on the factory, not concrete classes.
Extensibility	Easy to add new types (e.g., Bird) with minimal client code changes.
"""

