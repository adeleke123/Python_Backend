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

Method overriding is the ability of a subclass to provide a different implementation of a method that is already provided by its superclass. In python, this is achieved by defining a method with the same name in the subclass as in the superclass.

"""
# Here are some examples of OOP concepts in Python:

#Class:

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof woof!")

    def wag_tail(self):
        print("Tail wagging...")
dog1 = Dog("Fido", "Golden Retriever", 3)
print(dog1.name) # Output: Fido
dog1.bark() # Output: Woof woof!
dog1.wag_tail() # Output: Tail wagging...

'''Inheritance is a mechanism by which one class can inherit the properties and methods of another class. The class that inherits is called the derived class, and the class that is inherited from is called the base class.

For example, you can create a subclass of Dog called WorkingDog that inherits all the properties and methods of the Dog class, but also has additional attributes and methods specific to working dog'''

class WorkingDog(Dog):
    def __init__(self, name, breed, age, job):
        super().__init__(name, breed, age)
        self.job = job

    def work(self):
        print(f"{self.name} is working as a {self.job}.")

dog2 = WorkingDog("Max", "German Shepherd", 5, "police dog")
print(dog2.name) # Output: Max
dog2.bark() # Output: Woof woof!
dog2.work() # Output: Max is working as a police dog.
    
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

""" You can create an instance of the Dog class by calling the class name and passing any required arguments to the class constructor (init method)
Inheritance is a mechanism by which one class can inherit the properties and methods of another class. The class that inherits is called the derived class, and the class that is inherited from is called the base class.

For example, you can create a subclass of Dog called WorkingDog that inherits all the properties and methods of the Dog class, but also has additional attributes and methods specific to working dogs."""

class WorkingDog(Dog):
    def __init__(self, name, breed, age, job):
        super().__init__(name, breed, age)
        self.job = job

    def work(self):
        print(f"{self.name} is working as a {self.job}.")

dog2 = WorkingDog("Max", "German Shepherd", 5, "police dog")
print(dog2.name) # Output: Max
dog2.bark() # Output: Woof woof!
dog2.work() # Output: Max is working as a police dog.
"""
Polymorphism is the ability of a single function or method to operate on multiple types of data. In Python, polymorphism is achieved through method overriding and method overloading.

Method overriding is when a derived class provides a different implementation of a method that is already defined in the base class.

Method overloading is when a class defines multiple methods with the same name but different parameters.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof Woof"

c = Cat("Whiskers")
print(c.speak()) # Output: Meow

d = Dog("Fido")
print(d.speak()) # Output: Woof Woof
"""
In the above example, the base class Animal has a speak() method that is left empty (using the pass statement) because it is meant to be overridden by derived classes. The Cat and Dog classes both inherit from the Animals class and provide their own implementation of the speak() method. This allows for polymorphism, where a single function (in this case, speak()) can be called on objects of different classes (Cat and Dog) and produce different results.

Another example of polymorphism is the use of the + operator on different data types. In Python, the + operator can be used to add numbers, concatenate strings, and even merge lists. This is because the + operator is overloaded for different data types in Python.
"""

print(1 + 2) # Output: 3
print("Hello" + " " + "world!") # Output: "Hello world!"
print([1, 2, 3] + [4, 5, 6]) # Output: [1, 2, 3, 4, 5, 6]

"""In conclusion, OOP in Python provides several features to support OOP such as class, object, inheritance, and polymorphism. Classes are used to define the structure of objects and their methods, inheritance allows for code reuse and polymorphism allows for flexibility in how methods are implemented and used. These features allow for more modular, maintainable, and extensible code."""
