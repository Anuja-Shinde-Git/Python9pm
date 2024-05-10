# polymorphism

# 1.method overloading
# 2.duck typing
# 3.operator overloading
# 4.method overriding

# method overloading

class Calculator:

    def addition(self,x=None,y=None,z=None,a=None):

        if x != None and y != None and z != None and a != None:
            print(x+y+z+a)

        elif x != None and y != None and z != None:
            print(x+y+z)

        elif x!= None and y != None:
            print(x+y)

cc = Calculator()

cc.addition(12,3,4,5)
cc.addition(12,3,4)
cc.addition(12,3)

# duck typing

# program 1

class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hi hello")

def call_talk(obj):
    obj.talk()

a = Duck()
b = Human()

call_talk(a)
call_talk(b)


# program 2

class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hi hello")

class Dog:
    def bark(self):
        print("bow bow")


# def call_talk(obj):
#     if hasattr(obj,'bark'):
#         obj.bark()

# or 

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()

a = Duck()
b = Human()       
c = Dog()

call_talk(a)
call_talk(b)
call_talk(c)

# operato overloading
# program 3

print(1+1)
print("hi"+"hello")

class BookA:
    def __init__(self,pages):
        self.pages = pages

class BookB:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages+other.pages

ramayan = BookA(100)
mahabharat = BookB(200)

print(mahabharat+ramayan)
        
# program 4

class BookA:
    def __init__(self,pages):
        self.pages = pages

class BookB:
    def __init__(self,pages):
        self.pages = pages

    def __gt__(self,other):
        return self.pages > other.pages

ramayan = BookA(100)
mahabharat = BookB(200)

print(mahabharat > ramayan)

# method overriding

class WorldBank:

    def loan(self):
      print("I am loan from WB")

    def save(self):
        print("I am save from WB")

class SBI(WorldBank):
    pass

class PNB(WorldBank):
    pass

nagpur = SBI()
wardha = PNB()

nagpur.loan()
wardha.save()

# in above code use inheritance in class sbi and class pnb hence method from class WB wil inherited just using class and pass

# now we use separate methods for class SBI and class PNB with WB inheritance and still we get separate methods of class
# that is call method overriding

class WorldBank:

    def loan(self):
        print("I am loan from WB")

    def save(self):
        print("I am save from WB")

class SBI(WorldBank):

    def loan(self):
        print("I am loan from SBI")

    def save(self):
        print("I am save from SBI")

class PNB(WorldBank):

    def loan(self):
        print("I am loan from PNB")

    def save(self):
        print("I am save from PNB")

nagpur = SBI()
wardha = PNB()

nagpur.loan()
nagpur.save()

wardha.loan()
wardha.save()

