# MRO ==> Method Resolution Order

# if class is derived from more than one parent then it is called multiple inheritance
# and in that case MRO takes place. ie. same method is present in multiple class (parent and child) then how the flow of code flows
# method is called from which class that technique called MRO
# it search first in child/current class itself and then search in parent class in depth first, left to right manner 
# without searching the same class twice.

# program 1 

class A(object):
# each class derived/inherited by object wether (object) is mentioned or not
    def method(self):
        print('A class is called')
        super().method()

class B(object):
    def method(self):
        print('B class is called')
        super().method()

class C(object):
    def method(self):
        print('C class is called')

class X(A,B):
    def method(self):
        print('X is called')
        super().method()

class Y(B,C):
    def method(self):
        print('Y is called')
        super().method()

class P(X,Y,C):  
    def method(self):
        print('P is called')
        super().method()

p = P()
p.method()

# print(P.mro())  to get flow

# 1st it goes to current class ie. class P
# 2nd it goes to immediate parent of p ie. class X
# 3rd it goes to immediate parent of x ie. class A then class A has no parent  A is itself parent
# 4th it back to current class and goes to second immediate parent ie. class Y
# 5th it goes to immediate parent of y ie. class B then class B has no parent B is itself parent
# 6th it back to current class and goes to next immediate parent ie. class C and class C has no parent C is itself parent

# program 2

