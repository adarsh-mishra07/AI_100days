class Test:
    x=5
    def __init__(self):
        self.x=10
        self.y=20

T1=Test()
print(T1.x," and ",T1.y)



#one class has one class object and  many instance objects can be created from that class. The class object is created when the class is defined and it is used to create instance objects. The instance objects are created when the class is instantiated. The instance objects can access the class variables and methods using the class object.
#class object is created when the class is defined and it is used to create instance objects. The instance objects are created when the class is instantiated. The instance objects can access the class variables and methods using the class object.
#class var is static variable and it is shared among all the instance objects of the class. The instance var is a non-static variable and it is unique to each instance object of the class. The instance var can be accessed using the instance object and the class var can be accessed using the class object.
#initially,insatnce var is empty

# way of instance var
# 1. __init__(self) : method  - 

"""
 class Test:
    x=5
    def __init__(self):
        self.x=10
        self.y=20

T1=Test()     -> implicitly T1 object is passing in the class
print(T1.x," and ",T1.y)
 """