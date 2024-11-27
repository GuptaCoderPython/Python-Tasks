# 1. Define a static variable and access it through a class
class MyClass1:
    static_variable = "I am static!"

print(MyClass1.static_variable)

# 2. Define a static variable and access it through an instance
class MyClass2:
    static_variable = "I am still static!"

instance2 = MyClass2()
print(instance2.static_variable)

# 3. Define a static variable and change it within an instance
class MyClass3:
    static_variable = "Original value"

instance3 = MyClass3()
instance3.static_variable = "Instance value"

print("Instance value:", instance3.static_variable)
print("Class value:", MyClass3.static_variable)

# 4. Define a static variable and change it within the class
class MyClass4:
    static_variable = "Original value"

MyClass4.static_variable = "Changed value"

print("Class value:", MyClass4.static_variable)class A:
    # Two methods specific to A
    def methodA1(self):
        print("Method A1: Specific to class A")
    
    def methodA2(self):
        print("Method A2: Specific to class A")
    
    # Overridden method
    def overriddenMethod(self):
        print("Overridden method in class A")


class B(A):
    # Two methods specific to B
    def methodB1(self):
        print("Method B1: Specific to class B")
    
    def methodB2(self):
        print("Method B2: Specific to class B")
    
    # Overridden method
    def overriddenMethod(self):
        print("Overridden method in class B")


class C(B):
    # Two methods specific to C
    def methodC1(self):
        print("Method C1: Specific to class C")
    
    def methodC2(self):
        print("Method C2: Specific to class C")
    
    # Overridden method
    def overriddenMethod(self):
        print("Overridden method in class C")


def main():
    # Creating objects for each class
    a_object = A()
    b_object = B()
    c_object = C()

    # Calling methods of class A
    print("Class A Methods:")
    a_object.methodA1()
    a_object.methodA2()
    a_object.overriddenMethod()  # Calls A's version of the method

    # Calling methods of class B
    print("\nClass B Methods:")
    b_object.methodA1()  # Inherited from A
    b_object.methodA2()  # Inherited from A
    b_object.methodB1()
    b_object.methodB2()
    b_object.overriddenMethod()  # Calls B's version of the method

    # Calling methods of class C
    print("\nClass C Methods:")
    c_object.methodA1()  # Inherited from A
    c_object.methodA2()  # Inherited from A
    c_object.methodB1()  # Inherited from B
    c_object.methodB2()  # Inherited from B
    c_object.methodC1()
    c_object.methodC2()
    c_object.overriddenMethod()  # Calls C's version of the method

    # Polymorphism with superclass reference
    print("\nUsing superclass reference for runtime polymorphism:")
    a_ref = C()  # A reference to an object of class C
    a_ref.overriddenMethod()  # Calls C's version of the method


if __name__ == "__main__":
    main()

instance4 = MyClass4()
print("Instance value:", instance4.static_variable)