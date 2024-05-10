# 5 march 2024

# error 
# def addA(x,y):
#     print(x+y)

def addA(x,y):
    print(x+y)
addA(3,4)

# # default arguments

def addA(x=7,y=3):
    print(x+y)
addA()
addA(12,3)    

# positional argument

def addC(x,y):
    print(x+y)
addC(12,3)

# will not store in variable e as we not used return
e0 = addC(12,3)
print(e0)


def addD(x,y):
    return x+y
e = addD(12,3)
print(e)

def subC(x,y):
    return x-y
e2=subC(19,e)
print(e2)

# positional argument
def sub(x,y):
    print(x-y)
sub(y=33,x=50)    

# program 4
# want add all elements,don't konw how many no of there so use *args

def addD(*args):
    print(args)
    total=0
    for i in args:
        total = total+i
    return total
e3=addD(1,2,33,44,55,66,2,36,78,)    
print(e3)

# program 5
# want to collect all the elements use **kwargs will return dictionary
def addinfo(**kwargs):
    print(kwargs)
    kwargs['city']='pune'
    return kwargs    
e4=addinfo(first_name='chinmay',last_name='despande',age='34')
print(e4)

# Local and Global Variable
# program 6
def myfunction():
    a=1
    b=2
    a=a+1
    print(a)
    # will return 2 as a=a+1 defined in function
    print(b)
    # 2
myfunction()
# print(a)
# will return 1 as print(a) out of function

# program 7

a= 1
# global
def myfunction2():
    b = 5
    a = 6
    # local
    a = a+1
    print(a)
    # will return 7 as value of a update within function
    print(b)
myfunction2()
print(a)    
# will return 1 as we set global variale before the function

# program 8
a = 10
# global
def myfunction3():
    print(a)
    # global
    print(10)
myfunction3()
print(a)
# global

# program 9

h=10
# global
def myfunction4():
    global h
    h=99
    print(h)
    # 99 as global h updated
myfunction4()
print(h)  
# 99 as global h updated  

