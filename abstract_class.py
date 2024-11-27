from abc import ABC, abstractmethod

# Task 1: Create an abstract class with abstract and non-abstract methods
class BaseExample(ABC):
    @abstractmethod
    def perform_task(self):
        pass

    def show_message(self):
        print("This is a non-abstract method in the abstract class.")

# Task 2: Create a subclass for the abstract class
class DerivedExample(BaseExample):
    def perform_task(self):
        print("Abstract method implemented in the subclass.")
    
    def __init__(self):
        BaseExample.show_message(self)

# Task 3: Create an object for the abstract class in the child class and access the non-abstract methods
derived_instance = DerivedExample()

# Task 4: Create an instance for the child class and call the abstract and non-abstract methods
derived_instance.perform_task()
derived_instance.show_message()