#create a class employee with attributes,empid,name,salary and define methods to access properties of employee

class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid
    def getEmpid(self):
        return self.empid
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setSalary(self,salary):
        self.salary=salary
    def getSalary(self):
        return self.salary

E=Employee()
E.setEmpid(101)
E.setName("Adarsh Mishra")
E.setSalary(60000)
print("Employee ID:",E.getEmpid())
print("Employee Name:",E.getName()) 
print("Employee Salary:",E.getSalary()) 