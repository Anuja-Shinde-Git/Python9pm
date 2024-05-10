# program 1

class Person:
    country = "INDIA"
    def __init__(self,fn,ln,rollno,age):
        self.firstName = fn
        self.lastName = ln
        self.rollNo = rollno
        self.age = age
 
    def displayName(self):
        print(self.firstName + " " + self.lastName)

    def Updateage(self,ag):
        self.age = ag

rama = Person("rama","pawar",45,32)
print(rama.firstName)
print(rama.lastName)
print(rama.rollNo)
print(rama.age)
print(rama.country)

rama.country = "BHARAT"

sumit = Person("sumit","pawar",46,43)
print(sumit.country)
print(rama.country)

sumit.Updateage(13)
print(sumit.age)

# program 2

class Person:
    country = "INDIA"
    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

    # class method
    @classmethod
    def UpdateCounrty(cls,country):
        cls.country = country

    def Updateage(self,ag):
        self.age = ag

sam = Person("sam","jedhe",23)
ram = Person("ram","dhule",24)
man = Person("man","singh",25)            

print(ram.country)
print(sam.country)
print(man.country)

# class level method should be call over class
Person.UpdateCounrty("BHARAT")

print(ram.country)
print(sam.country)
print(man.country)


# program 3
# count of object

class Vehical:
    count = 0 
    country = "INDIA"

    def __init__(self,color,type):
        self.color = color
        self.type = type
        Vehical.count = Vehical.count+1

    # instance method
    def updateColor(self,cl):
        self.color = cl

    # class method
    @classmethod
    def UpdateCounrty(cls,cnty):
        cls.country = cnty

    # static method  
    @staticmethod
    def countObj():
        print(Vehical.count)

audi = Vehical("blue","sedane")
bmw = Vehical("red","SUV")
mahindra = Vehical("black","THAR")       

print(audi.country)
print(bmw.country)
print(mahindra.country)

Vehical.UpdateCounrty("BHARAT")

print(audi.country)
print(bmw.country)
print(mahindra.country)

Vehical.countObj()