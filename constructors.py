# Task 1: Write a class with a default constructor, one argument constructor, and two argument constructors.
class MyClass:
    # Default constructor
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called")
        elif arg2 is None:
            print(f"One argument constructor called with argument: {arg1}")
        else:
            print(f"Two argument constructor called with arguments: {arg1}, {arg2}")

class MainClass:
    def __init__(self):
        print("MainClass constructor called")
        MyClass()               # Default constructor
        MyClass("Argument")     # One argument constructor
        MyClass("Arg1", "Arg2") # Two argument constructor

main_instance = MainClass()

# Task 2: Call the constructors (both default and argument constructors) of the super class.
class SuperClass:
    def __init__(self, arg=None):
        if arg is None:
            print("SuperClass default constructor called")
        else:
            print(f"SuperClass constructor with argument: {arg}")

class SubClass(SuperClass):
    def __init__(self):
        super().__init__()
        print("SubClass constructor called")

subclass_instance = SubClass()

# Task 3: Apply private, public, protected, and default access modifiers to the constructor.
class MyClass:
    def __init__(self):
        print("Public constructor called")

    def _protected_constructor(self):
        print("Protected constructor called")

    def __private_constructor(self):
        print("Private constructor called")

class MainClass:
    def __init__(self):
        print("MainClass constructor called")
        my_obj = MyClass()
        my_obj._protected_constructor()  # Accessible within the class or subclass

main_instance = MainClass()

# Task 4: Write a program which illustrates the concept of attribute constructor.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, {self.age} years old")

person_instance = Person("Neeraj", 20)