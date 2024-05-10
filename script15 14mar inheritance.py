# Inheritance

# properties in one class that are same in other class then we are not going to rewrite and makes code lengthy we can use properties
# mentioned in 1st class in all other class is called inheritance

# types of inheritance
# 1. Single inheritance
# 2. Multilevel inheritance
# 3. Hierarchical inheritance
# 4. Multiple inheritance ==> only in python

# program 1

class Student:
    def __init__(self,fn,ln,aadhar):
        self.firstName = fn
        self.lastName = ln
        self.aadhar = aadhar

    def displayName(self):
        print(self.firstName + ' '+ self.lastName)    

class Teacher(Student):
    salary = 10000
    # we created 2nd class without using constructor but because of inheritance all the properties in 1st class we can call on this
    # also we can create object on teacher

    def displaySalary(self):
        print(self.salary)


amar = Teacher("amar","niraml",1234)
print(amar.firstName)
print(amar.lastName)
print(amar.aadhar)
print(amar.salary)

amar.displayName()
amar.displaySalary()


# Single inheritance

# program 2

class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNO = adharNo

    def displayName(self):
        print(self.firstName+' '+self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,adharNo,salary):
        # here we use constructor with parents class value and extra child class value
        super().__init__(fn,ln,adharNo)
        # here we use super__init__ method as we use parents class values also
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

shubham = Teacher("shubham","kade",1234,15000)
# child's reference variable
# we can call four properties and two methods on it
print(shubham.firstName)
print(shubham.lastName)
print(shubham.adharNO)
print(shubham.salary)

shubham.displayName()
shubham.displaySalary()

        
# multilevel inheritance

# program 3

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName= ln

    def displayGName(self):
        print(self.firstName + ' ' + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)        
        self.fname = ffn

    def displayFname(self):
        print(self.fname + ' ' + self.lastName)   

class Son(Father):
    def __init__(self,fn,ln,ffn,sn):
        super().__init__(fn,ln,ffn)
        self.sname = sn

    def displaySname(self):
        print(self.sname+ ' '+self.lastName)

sanket = Son("shankarrao","shinde","anil","sanket")

print(sanket.sname)
print(sanket.fname)
print(sanket.firstName)
print(sanket.lastName)

sanket.displayGName()
sanket.displayFname()
sanket.displaySname()

