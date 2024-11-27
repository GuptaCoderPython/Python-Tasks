#Task 1  Write two methods with the same name but different numbers of parameters of the same type.
class OverloadExample1:
    def display(self, a, b=None):
        if b is None:
            print(f"Single parameter: {a}")
        else:
            print(f"Two parameters: {a}, {b}")

obj = OverloadExample1()
obj.display(5)
obj.display(5, 10)

#task2 Write two methods with the same name but different numbers of parameters of different data types.
class OverloadExample2:
    def display(self, param):
        if isinstance(param, int):
            print(f"Integer parameter: {param}")
        elif isinstance(param, str):
            print(f"String parameter: {param}")

obj = OverloadExample2()
obj.display(5)
obj.display("Hello")


#task3 Write two methods with the same name and the same number of parameters of the same type.
class OverloadExample3:
    def display(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            print(f"Addition: {a + b}")
        elif isinstance(a, float) and isinstance(b, float):
            print(f"Multiplication: {a * b}")

obj = OverloadExample3()
obj.display(5, 10)
obj.display(5.5, 2.0)