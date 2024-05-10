# class is user defined datatype

# program 1

class Person:

    first_name = "shivraj"
    last_name = "shinde"
    age = 16

    def display(self):
        print(self.first_name + self.last_name)


shivraj = Person()
print(shivraj.first_name)
print(shivraj.last_name)
print(shivraj.age)

shivraj.display()

# if we created new object the values will not change as we used templet so we need to update values each time
shraddha = Person()
print(shraddha.first_name)
print(shraddha.last_name)
print(shraddha.age)
shraddha.display()

shraddha.first_name = "shraddha"
print(shraddha.first_name)

# problem is we cant update values each time so solution is define constructor in run time creation of object
# also we can add new propertise to object 

# program 2

class Person:

    def __init__(self,fn,ln,age):
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def display(self):
        print(self.first_name + self.last_name)

    def displayAge(self):
        print(self.age)    

amol = Person("amol","rao",30)
amol.display()
amol.displayAge()
print(amol.first_name)
print(amol.last_name)
print(amol.age)

chinmay = Person("chinmay","deshpande",35)
chinmay.display()
chinmay.displayAge()
print(chinmay.first_name)
print(chinmay.last_name)
print(chinmay.age)

shraddha = Person("shraddha","kane",23)

# want to print all the methods for all the objects at a time wrap them in a list

students = ["amol","chinmay","shraddha"]
# data type amol,chinmay,sharddha is person ie class we defined class person and followed that

students = [amol,chinmay,shraddha]
for student in students:
    student.display()
    student.displayAge()
    
# program 3
    
class Vehical:

    def __init__(self,color,type):
        self.color = color
        self.type = type

    def displayColor(Self):
        print(Self.color)

audi = Vehical("red","sedane")
bmw = Vehical("blue","SUV")

audi.displayColor()
bmw.displayColor()
