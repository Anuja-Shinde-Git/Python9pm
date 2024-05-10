# program 1 
# formal arguments ==> x,y
# actual arguments ==> 12,13

def add(x,y):
    return x+y
e = add(12,13)
print(e)


# program 2 'positional argument'

def sub(x,y):
    return(x-y)

e2 = sub(y=35,x=45)
print(e2)


# program 3 'default argument'

def mul(x=3,y=5):
    return(x*y)

e3 = mul()  
print(e3)
e4 = mul(4,5)
print(e4) 


# program 4 'variable length arguments'

def addAll(*args):
# "*" is mandatory
 print(args)
 total = 0
 for i in args:
  total = total + i
 return total

e5 = addAll(1,2,3,4,5,6,73,4,5,6,6,55,6,7,3,4,5,6,7)
print(e5)


# program 5 

def greet(*args):
   for i in args:
      print("welcome " + i)

greet("pune","mumbai","nagpur","delhi")      


# program 6 
def printInfo(**kargs):
   print(kargs)
   for i in kargs:
      print(i,kargs[i])

printInfo(firstname = 'chinmay', lastname = 'despande',age=34,city= 'pune')      










