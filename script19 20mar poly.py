# Polymorphism

# 2.Duck typing

# in duck typing same method is present in all the classes if the required behavior is present in that object the python doesnt care 
# about which class of object it is if it ab object and required behavior is present for that object then it will work

# in below exaple we create 2 class both class have same method that is same behavior 

# program 1
# class 1
class Duck:
    def talk(self):
        print("quack quack")

# class 2
class Human:
    def talk(self):
        print("hi hello")

# here out of class one method created to call talk method. pass one object.once the object pass to the call method talk method 
 # will be called
        
def call_talk(obj):
    obj.talk()

# object created
duckA = Duck()
sanket = Human()

call_talk(duckA)
# on Duck's object duckA called call method so this will call talk method of Duck class on Duck's object duckA

call_talk(sanket)
# on Human's object sanket called call method so this will call talk method of Human class on Human's object sanket


# now what if the method is different for one class so this will not run so recover this we use strong typing
# i.e we use has attribute hasattr(object,'attribute')ie.(obj,'methodname') method

# program 3

# class 1
class Duck:
    def talk(self):
        print("quack quack")

# class 2
class Human:
    def talk(self):
        print("hi hello")

# class 3 with bark method different method
class Dog:
    def bark(self):
        print("bow bow")

# here we use hasattr() with if else block to run both the method
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()    

duckA = Duck()
sanket = Human()
jimmy = Dog()

call_talk(duckA)
call_talk(sanket)
call_talk(jimmy)



# practice

# program 1

class Duck:
    def walk(self):
        print("thapak thapak")

class Horse:
    def walk(self):
        print("thabadak thabadak")

def call_walk(obj):
    obj.walk()

d = Duck()
h = Horse()

call_walk(d)
call_walk(h)

# program 2

class Duck:
    def walk(self):
        print("thapak thapak")

class Horse:
    def walk(self):
        print("thabadak thabadak")

class Dog:
    def talk(self):
        print("bow bow")

def call_walk(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    else:
        obj.talk()

d = Duck()
h = Horse()
d1 = Dog()

call_walk(d1)


# 3.Operator overloding

print(1+1)
print("hello"+"world")

# so here '+' operator act differently with int and differently with str
# if any of the operator performs additional action other than what it is meant for is called operator overloading

# in below example we will achive required o/p of mathematical operator using objects directly

class BookA:
    def __init__(self,pages):
        self.pages = pages

class BookB:
    def __init__(self,pages):
        self.pages = pages

ramayan = BookA(100)
mahabharat = BookB(200) 

print(ramayan.pages+mahabharat.pages)
# this will makes sense and will give o/p with addition of pages of both the books

# but my requirment is using objects directly it should perform addition od pages
# print(object + object)
# print(ramayan + mahabharat)

# so here we use method overriding __add__ method with return // __add__(self,other) return

class BookA:
    def __init__(self,pages):
        self.pages = pages

class BookB:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return (self.pages + other.pages)            
    
ramayan = BookA(100)
mahabharat = BookB(200)

# print(ramayan + mahabharat)  here this will not give o/p as we declared method in class BookB i.e for mahabharat so it will add
# mahabharat with ramayan 1st should be mahabharat

print(mahabharat + ramayan)

# and for adding ramayan with mahabharat we should declare add method in class BookA

class BookA:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return (self.pages + other.pages)

class BookB:
    def __init__(self,pages):
        self.pages = pages

ramayan = BookA(100)
mahabharat = BookB(200)

print(ramayan + mahabharat)



