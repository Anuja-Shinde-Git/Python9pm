
# single inheritance

# program 1

class Student:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def displayName(self):
        print(self.firstname+ ' '+self.lastname)

class Teacher(Student):
    def __init__(self, fn, ln,salary):
        super().__init__(fn, ln)    
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

aashish = Teacher("aashish","kame",10000)

print(aashish.firstname)
print(aashish.lastname)
print(aashish.salary)

aashish.displayName()
aashish.displaySalary()

# multilevel inheritance

# program 2

class Student:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def displayName(self):
        print(self.firstname+ ' '+self.lastname)

class Teacher(Student):
    def __init__(self, fn, ln,salary):
        super().__init__(fn, ln)     
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

class Professor(Teacher):
    def __init__(self, fn, ln, salary,spe):
        super().__init__(fn, ln, salary)   
        self.specialization = spe

    def displaySpecialization(self):
        print(self.specialization)

hitesh = Professor("hitesh","sharma",100000,"testing")

print(hitesh.firstname)
print(hitesh.lastname)
print(hitesh.salary)
print(hitesh.specialization)

hitesh.displayName()
hitesh.displaySalary()
hitesh.displaySpecialization()

# hierarchical inheritance

# program 3

class Mother:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def displayName(self):
        print(self.firstname+" "+self.lastname)

class Son(Mother):
    def __init__(self, fn, ln,sn):
        super().__init__(fn, ln)            
        self.sname = sn

    def displaySname(self):
        print(self.sname+" "+self.lastname)

class Daughter(Mother):
    def __init__(self, fn, ln,dn):
        super().__init__(fn, ln)  
        self.dname = dn

    def displayDname(self):
        print(self.dname+' '+self.lastname)

bhushan = Son("dipika","dongare","bhushan")

print(bhushan.firstname)
print(bhushan.lastname)
print(bhushan.sname)
bhushan.displayName()
bhushan.displaySname()

mayuri = Daughter("dipika","dongare","mayuri")
print(mayuri.firstname)
print(mayuri.lastname)
print(mayuri.dname)

mayuri.displayDname()
mayuri.displayName()

# multiple inheritance

# in multiple inheritance flow of code is as per sequence we keep while creating child class inheritance.
# one more method to identify the flow put 'print("mother constructor called")' and 'print("mother constructor called")'
#  command in both the parants constructor

# program 4

class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstname = fn
        self.lastname = ln

    def displayname(self):
        print(self.firstname+' '+self.lastname)

class Father:
    def __init__(self,fn,ln):
        print("father constructor called")
        self.firstname = fn
        self.lastname = ln

    def displayName(self):
        print(self.firstname+' '+self.lastname)

class Son(Mother,Father):
    def __init__(self, fn, ln,sn):
        super().__init__(fn, ln)
        self.sname = sn

    def displaySname(self):
            print(self.sname+' '+self.lastname)

aniket = Son("surekha","shinde","aniket")

print(aniket.firstname)
print(aniket.lastname)
print(aniket.sname)

aniket.displayname()
aniket.displaySname()



