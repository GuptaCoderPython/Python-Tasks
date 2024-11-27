class PrivateExample:
    def __init__(self):
        self.__private_field = "This is a private field"
    
    def __private_method(self):
        print("This is a private method")
    
    def access_private(self):
        print("Accessing private method from within the class:")
        self.__private_method()
        print("Private field:", self.__private_field)


class ProtectedExample:
    def __init__(self):
        self._protected_field = "This is a protected field"
    
    def _protected_method(self):
        print("This is a protected method")