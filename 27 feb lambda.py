# lambda function

def addA(x,y):
    return(x+y)
    
e = addA(4,2)
print(e)


# program 1

def addition (fn,x,y):
    # fn = lambda x,y : x+y
    # x = 12
    # y = 4
    e = fn(x,y)
    return(e)  

add = lambda x,y : x+y

result= addition (add,12,4)
print(result)


# program2
# function as a parameter to another function
sub = lambda x,y : x-y
def subtraction (fn,x,y):
    # fn = lambda x,y : x-y
    # x = 12
    # y = 4
    e = fn(x,y)
    return e
print(e)
  
result2 = subtraction(sub,12,4) 
print(result2)


# x = 10 
# print(x)

# print(sub) function  (sub = lambda x,y : x-y)

# e=sub(23,3) function all
# print(e)


# program 3
# function as a return type

def multuplication():
    return lambda x,y: x*y

result3 = multuplication()
# print(result3) lambda x,y: x*y
e2 = result3(34,5)
print(e2)



