#  Polmorphism

# if a same method is called to get multiple results is called polymorphism
# poly means many and morphs means forms so it is derived from that many forms of result by one method

# Polymorphism has mainly two types in other language (java)  
# 1. method overloading and 
# 2. method overriding

# but python has 4 types
# 1. method overloding
# 2. method overriding
# 3. duck typing
# 4. operator overloading

# 1. method overloading
# same class same method name different signiture/result

# program 1

# class Calculator:
#     def addition(self,x,y):
#         print(x+y)

#     def addition(self,x,y,z):
#         print(x+y+z)    

#     def addition(self,x,y,z,a):
#         print(x+y+z+a)

# # Calculator()   object created wether stored in variable or not object will create
        
# cc = Calculator() 
# cc.addition(12,3)
# cc.addition(12,3,4)
# cc.addition(12,3,4,5)
    
#  in python same method called in one class then it will pickup last one most updated one, python will consider all methods as one single method
# so in above code error will occur as
# TypeError: Calculator.addition() missing 2 required positional arguments: 'z' and 'a'

# so to overcome this problem we have to set by default value none to the paramter while creating the method
# as if values are not provided then it will consider as none
                

class Calculator:

    def addition(self, x=None, y=None, z=None, a=None):
        if x != None and y != None and z != None and a != None:
           print(x+y+z+a)

        elif x != None and y != None and z != None:
            print(x+y+z)

        elif x != None and y != None:
            print(x+y)    

cc = Calculator()
cc.addition(12,3)
cc.addition(12,3,4)
cc.addition(12,3,4,5)