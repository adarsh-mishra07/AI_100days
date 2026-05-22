'''



class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def show_details(self):
        print("Name:",self.name)
        print("Roll No",self.roll)
        print("Marks",self.marks)

s1=Student("Adarsh",208,95)
s1.show_details()

'''


