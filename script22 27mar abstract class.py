# Abstract method

# worldbank ---- save() loan()
# SBI -------- save() loan()
# ICICI ----- save() loan()

# complete abstraction ---- method definition
# partial abstraction ----- complete method abstract


# in abstract method need to import ABC from abc >> ABC is package from abc library
# we have define @abstractmethod decorator before method declaration to make that method abstract method
# abstract class has only body
# we can not create objects of abstract class


# program 1

from abc import ABC , abstractclassmethod

class WorldBank(ABC):
    @abstractclassmethod
    def loan(self,x):
        pass
    @abstractclassmethod
    def save(self,x):
        pass

# we can not create object of abstract class 

# a = WorldBank()

class SBI(WorldBank):
    # loan
    def loan(self,x):
        print("loan is" + str(x))

    # save
    def save(self,x):
        print("save is"+ str(x))

    def branchname(self):
        print('pune')    

class PNB(WorldBank):

    def loan(self,x):
        print("loan is"+ str(x))

    def save(self,x):
        print("save is"+ str(x))

    def branchname(self):
        print('pune')

a = SBI()
a.save(13)
a.loan(3)

b = PNB()



# program 2

from abc import ABC, abstractclassmethod

class WorldBank(ABC):

    @abstractclassmethod
    def loan(self):
        pass
    
    @abstractclassmethod
    def save(self):
        pass

    def country(self):
        print("INDIA")


class SBI(WorldBank):

    def loan(self):
        print("loan from SBI")

    def save(self):
        print("save from SBI")

class PNB(WorldBank):

    def loan(self):
        print("loan from PNB")

    def save(self):
        print("save from PNB")    

a = SBI()
b = PNB()

a.save()
a.loan()
a.country()

b.save()
b.loan()
b.country()

# here we can access 3 mehods save , loan and country also as country is defined in parent class but for common use 
# without making ith abstractmethod






