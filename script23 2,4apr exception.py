# compile time error >> syntax error

# program 1
# def add():
# print(3+4)

# run time error >> error depends on user input

# program 2
# x = int(input('enter numberA'))
# y = int(input('enter numberB'))
# print(x/y)
# ZeroDivisionError: division by zero

# listA = [11,22,33,44]
# print(listA[4])
# IndexError: list index out of range

# logical error >> error indroduced by coder 

# program 3  want salary plus 10percent salary

def calculateBonuceSalary(amount):
    return amount * 0.10 + amount

e = calculateBonuceSalary(1000)
print(e)

# calculate only 10 percent amount here error is in logic building by coder
def calculateBonuceSalary(amount):
    return amount * 0.10 

e = calculateBonuceSalary(1000)
print(e)


# program 4

# create generic exception and handled due to this code not terminated
# print('hello')
# try:
#     x = int(input('enter numberA'))
#     y = int(input('enter numberB'))
#     print(x/y)
# except Exception:
#     print('enter correct number')    
# print('bye')

# program 5

# try:
#     names = ['asha','usha','nisha','misha']
#     x = int(input('enter numberA'))
#     y = int(input('enter numberB'))
#     print(x/y)
#     print(names[3])
#     # print(a)
# except ArithmeticError:
#     print('enter correct value')
# except IndexError:
#     print('add more elements in list')
# except NameError:
#     print('not defined')            
# except Exception:
#     print('something went wrong')
# print('bye')    

# program 6
# finally block always executed irrespective to error/exception

# try:
#     names = ['surya','prakash','kiran','sawali']
#     x = int(input('enter numberA'))
#     y = int(input('enter numberB'))
#     print(x/y)
# except ArithmeticError:
#     print('please enter correct value')
# finally:
#     print('I will always execute')       


# program 7
# else block will run if error not raised

# try:
#     x = int(input('enter numberA'))
#     y = int(input('enter numberB'))
#     print(x/y)
# except ArithmeticError:
#     print('invalid input')
# else:
#     print('hello')        


# program 8

# print('hi')
# try:
#     x = int(input('enter numberA'))
#     y = int(input('enter numberB'))
#     print(x/y)
# except ArithmeticError:
#     print('invalid input')
# else:
#     print('hello')    
# finally:
#     print('I will always execute')
# print('bye')            


# a single try block can have multiple except blocks >> TRUE
# multiple except block can handle multiple exceptions >> TRUE
# we cannot write except block without try block >> TRUE
# we cannot write try block without except block >> FALSE
# else and finally blocks are not compulsory >> TRUE
# when there is no exception else block will execute after try block >> TRUE
# finally block is always executed


# logical error

def calAvg(list):
    total = 0
    for i in list:
        total = total + i
    avg = total/len(list) 
    return total,avg

try:
    t,a = calAvg([])
    print(t)
    print(a)
except TypeError:
    print('type error')
except ZeroDivisionError:
    print('zero division,can not pass empty list')
except Exception:
    print('error')    

# need to practice

# Assert

# print("hello")
# try:
#     x = 18
#     assert x > 1 and x <= 9
#     print(x)
# except AssertionError:
#     print("condition not matched")
# print("bye")
# try:
#     x = int(input('Enter the number :'))
#     y = 1/x
# finally:
#     print("We are not catching the exceptions..")
# print("The inverse is ",y)

# handling the Assertion 

# try:
#     x = int(input("Enter the number between 5 and 10"))
#     assert x >= 5 and x <= 10
#     print("the number enter is ",x)
# except AssertionError:
#     print("The condition is not fulfilled")


class lowBalance(Exception):
    def __init__(self,msg):
        self.msg = msg

def check(dict):
    for k,v in dict.items():
        if(v < 20000):
            raise lowBalance("the value is below 20k , please add amount")

try:
   bank = {"raj":100000,"shivani":90000,"chinmay":100000,"tavish":50000}
   check(bank)
   print("all above 20 thousand")
except lowBalance as me:
        print(me)