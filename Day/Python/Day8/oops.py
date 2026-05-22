class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"Name:{self.name}, Age:{self.age}")


#create object 
s1=Students("Adarsh",21)
s1.show()


#coustructor 
class Car:
    wheels=4   #class variable
    def __init__(self,name):
        self.name=name     #instance variable 
    
car1=Car("BMW")
print(f"car name={car1.name} and ,car wheels={Car.wheels}")



#inheritance

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

d = Dog()
d.sound()



#polymorphism

def add(a,b,c=0):
    return a+b+c
print(add(2,3))
print(add(2,3,4))


#encapsulation

class Account:
    def __init__(self,balance):
        self.__balance=balance
    
    def show_balance(self):
        print("Balance:",self.__balance)

a1=Account(1000)
a1.show_balance()


#Abstraction - using Abstract class:

from abc import ABC ,abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self,a):
      self.a=a
      pass
  
class Circle(Shape):
      def area(self,a):
          self.a=a
          print("Area of circle=",self.a)

c=Circle()
c.area(10)