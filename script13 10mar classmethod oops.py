# program 1
class Person:
    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

    def displayName(self):
        print(self.firstName +' '+ self.lastName)

ram = Person("ram","swami",34)
ram.displayName()           
print(ram.firstName)
print(ram.lastName)
print(ram.age)

# program 2

class Person:
    # class variable
    country = 'India'
    def __init__(self,fn,ln,age,salary):
        self.firstName = fn
        self.lastName = ln
        self.age = age
        self.salary = salary

    # instance method
    def displayName(self):
        print(self.firstName + ' '+ self.lastName)

    def UpdateSalary(self,sl):
        self.salary = sl

sham = Person("sham","yadav",23,10000)
balram = Person("balram","yadav",24,20000)

print(sham.country)
print(balram.country)

sham.country = "BHARAT"

print(sham.country)
# BHARAT
print(balram.country)
# INDIA as we only updated for sham 
