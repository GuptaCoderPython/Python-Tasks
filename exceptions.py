#task1 Write a program to generate an ArithmeticException without exception handling.

result = 10 / 0
print(result)

#task2  Handle the ArithmeticException using try-except.

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
#task3 Write a method which throws an exception, and call that method in the main class without try block
def throw_exception():
    raise Exception("Custom exception thrown")

throw_exception()
#task4 Write a program with multiple catch blocks.

try:
    value = int("abc")
    result = 10 / 0     # This would raise ZeroDivisionError if reached
except ValueError as e:
    print(f"ValueError caught: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")

#task5 Write a program to throw an exception with your own message.

def custom_exception():
    raise Exception("This is a custom exception message")

try:
    custom_exception()
except Exception as e:
    print(f"Caught exception: {e}")

#task6 Write a program to create and use your own exception.
class CustomException(Exception):
    pass

try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print(f"Caught CustomException: {e}")


#task7  Write a program with a finally block.

try:
    print("Attempting risky operation...")
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught exception: {e}")
finally:
    print("This will execute no matter what.")

#ask8 Write a program to generate an ArithmeticException.

result = 10 / 0 #0div error.
#task9 Write a program to generate a FileNotFoundException.
with open("test.txt", "r") as file:
    content = file.read()

#this will throw the error because test.txt file is not present.


#task10  Write a program to generate a ClassNotFoundException.
import test  # This will raise ImportError

#task11 Write a program to generate an IOException.
import os
os.remove("test.txt")  # Raises FileNotFoundError, a subclass of OSError

#task12 Write a program to generate a NoSuchFieldException.

class Neeraj:
    pass

obj = Neeraj()
print(obj.non_existent_attribute)  # Raises AttributeError
