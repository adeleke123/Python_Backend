"""
Class inheritance is a feature in object-oriented programming languages like Python, which allows you to create a new class based on an existing class. The new class is called a derived class or a subclass and the existing class is called a base class or a superclass. The derived class inherits attributes and behaviors from the base class, and can also have its own unique attributes and behaviors.
Here's a simple example to illustrate class inheritance in Python:
"""
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self):
    print("Some generic animal sound")

class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="Dog")
    self.breed = breed

  def make_sound(self):
    print("Woof!")

dog = Dog("Fido", "Labrador")
dog.make_sound() # Output: Woof!
"""
In this example, we first create a base class Animal with two attributes name and species and a method make_sound. Then we create a derived class Dog that inherits from Animal. The Dog class has its own __init__ method that calls the __init__ method of the Animal class and sets its own attribute breed. The Dog class also overrides the make_sound method with its own implementation.
"""
