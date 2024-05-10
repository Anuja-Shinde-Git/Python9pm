# lambda function
# lambda

def add(x,y):
    return x + y

e = add(12,4)
print(e)

addB = lambda x,y:x+y
e2 = addB(21,4)
print(e2)
e = lambda x : x*x 
e3 = e(3)
print(e3)

names = ["amit","amol","akay","shivani"]
def changeName(lst):
    #lst = names 
    lst[0] = "ajay"
    return lst

e4 = changeName(names)
print(e4)
print(names)

# city = ["pune","nagpur","kolkata"]
# city2 = city 
# city2[0] = "wardha"
# print(city)
# print(city2)

lstA = [1,2,3,4,5]
n = []
for i in lstA:
    n.append(i*5)
print(n)

# list comprehension -- o/p - list
#[expression:loop:condition]
e4 = [i * 5 for i in lstA]
print(e4)
lstB = [1,2,3,4,5,6,7,8,9,10]
e5 = [i* i for i in lstB]
print(e5)

lstC = [44,55,66,77,33,44,55,66,77,11,22,33,7,8,9]
listD= []
for x in lstC:
    if x % 2 == 0:
        listD.append(x)
print(listD)

#[expression:loop:condition]
e6 =  [x for x in lstC if x % 2 == 0]
print(e6)

#-------------------------------------------------------------------------------------

# print fruits names in below list of fruits

fruits = ["apple","banana","mango","guva"]

names =[]
for i in fruits:
    names.append(i)
print(names) 


names = [i for i in fruits]
print(names)

# -----------------------------------------------------------------------------------------

# print square of odd numbers

numbers = [1,2,3,4,5,6,7,8,9]
square = []
for i in numbers:
    if i %2 != 0:
       square.append(i*i)
print(square)

square = [i*i for i in numbers if i %2 != 0]
print(square)

# --------------------------------------------------------------------------------------------

# print square of numbers

num = [1,2,3,4,5]
squ = []
for i in num:
    squ.append(i*i)
print(squ)

squ = [i*i for i in num]
print(squ)

# -----------------------------------------------------------------------------------------------

# print element in upper case

names = ['aashish','hitesh','kishor','jagdish']
namesUp = []
for i in names:
    namesUp.append(i.upper())
print(namesUp)


namesUp = [i.upper() for i in names]
print(namesUp)

# ---------------------------------------------------------------------------------------------

# print table of two

list = [1,2,3,4,5,6,7,8,9,10]
TableTwo = []
for i in list:
    TableTwo.append(i*2)
print(TableTwo)    


TableTwo = [i*2 for i in list]
print(TableTwo)

# -------------------------------------------------------------------------------------------------

# print current age

BirthYear = [1991,1992,1993,1994,1995,1996,1997,1998,1999,2000]
Age = []
for i in BirthYear:
    Age.append(2024-i)
print(Age)


Age = [(2024-i) for i in BirthYear]
print(Age)

# -------------------------------------------------------------------------------------------------------

# print elements above 40 

list2 = [27,34,67,88,40,56,98,76,59.89]
Above40 = []
for i in list2:
    if i > 40:
     Above40.append(i)
print(Above40)    


Above40 = [i for i in list2 if i > 40]
print(Above40)

# -----------------------------------------------------------------------------------------------------------

# print even numbers

number = [11,12,13,22,33,44,55,66,77,88,98,99,80]
Even = []
for i in number:
    if i%2 == 0:
        Even.append(i)
print(Even)


Even = [i for i in number if i%2 == 0]
print(Even)

# ----------------------------------------------------------------------------------------------------------

# print type of number in below list likewise even or odd

list3 = [12,33,22,41,14,56,77,74,89,99,78,56]
NumTyp = []

for i in (list3):
    if i % 2 == 0:
     NumTyp.append("even")
    else:
     NumTyp.append("odd")

print(NumTyp)


NumTyp = [("even" if i%2 ==0 else "odd") for i in list3]
print(NumTyp)


