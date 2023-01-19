""" OOP concept
Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code that manipulates that data. 

In Python, OOP concepts are implemented using classes and objects.

A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).

An object is an instance of a class, created at runtime. Objects have member variables and have access to methods defined in their class.

In Python, the class is created by the keyword class, and an object is created using the constructor of the class.

Inheritance allows new classes to be derived from existing classes. The derived class inherits the member variables and methods of the existing class, but can also have its own.

Encapsulation is the practice of keeping an object's internal state and behavior hidden from the outside world, and providing controlled access to that state and behavior via methods.

Polymorphism is the ability of a single function or method to operate on multiple types of data. In Python, polymorphism is achieved through method overloading and method overriding.

Method overloading is the ability of a class to have more than one method with the same name but different parameters. Python does not support method overloading.

Method overriding is the ability of a subclass to provide a different implementation of a method that is already provided by its superclass. In python, this is achieved by defining a method with the same name in the subclass as in the superclass

"""
# Here are some examples of OOP concepts in Python:

#Class:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

dog1 = Dog("Fido", "Golden Retriever")
dog2 = Dog("Buddy", "Labrador Retriever")

print(dog1.name)  # Output: Fido
print(dog2.breed)  # Output: Labrador Retriever
dog1.bark()  # Output: Woof!
