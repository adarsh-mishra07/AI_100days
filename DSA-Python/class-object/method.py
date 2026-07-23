"""
1.Instance methods are the methods that are defined inside the class and they are used to access the instance variables of the class. The instance methods are called using the instance object of the class. The instance methods can access the class variables and methods using the class object.
2. Class methods are the methods that are defined inside the class and they are used to access the class variables of the class. The class methods are called using the class object of the class. The class methods can access the instance variables and methods using the instance object.
3. Static methods are the methods that are defined inside the class and they are used to access the class variables of the class. The static methods are called using the class object of the class. The static methods can access the instance variables and methods using the instance object.
"""

class Test:
    x=5
    def __init__(self): #it is instance method and it is used to initialize the instance variables of the class. It is called when the class is instantiated. It takes self as a parameter which is the instance object of the class.
        self.x=10
        self.y=20
    def instance_method(self):
        print("This is an instance method")
        print("The value of x is:",self.x)
        print("The value of y is:",self.y)
    @staticmethod
    def static_method():
        print("This is a static method")
        print("The value of x is:",Test.x)
    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("The value of x is:",cls.x)

T1=Test()
print(T1.x," and ",T1.y)
T1.instance_method()

Test.static_method()
T1.static_method()
    
Test.class_method()
T1.class_method()