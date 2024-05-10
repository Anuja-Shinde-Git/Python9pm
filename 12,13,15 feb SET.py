# Set in Python
# unhashable i.e can be changed , we can edit SETS
# empty set is a dictionary
# set is an unorderd collection * of unique object **
# duplicates are not allowed
# indexing cant be used to acce the elements inside a set


# Creating a set

s1 = {11,22,33,44}
print(s1)
print(type(s1))

# Properties of SETS

# s2 = {11,22,33,44,[11,22,33]}
# print(s2)


s3 = {11,22,33,44,'one','two'}
print(s3)


# s4 = {11,22,33,44,'one','two',{99,88,77}}
# print(s4)

#  comparing the sets with differnt orders

s1 = {11,22,33,44}
print(s1)
print(type(s1))
print(id(s1))


s2 = {22,33,44,11}
print(s2)
print(type(s2))


print(s1==s2)


list_num1 = [11,22,33,44]
list_num2 = [22,33,44,11]

print(list_num2 ==list_num1)
#  HW
#  chekc the ID of each set and compare


# 

s5 = {10}
print(s5)
print(type(s5))


s6 = {}
print(s6)
print(type(s6)) #empty set is a dictionary

t1 = (10,11,12)
print(type(t1))

t2 = (99,)
print(type(t2))



# INdexing is not there in SETS

s7 = {22,33,44,11,22,33,44,11,22,33,44,11}
s8 = {22,33,44,11}

print(s7)
print(s8)
# print(s8[0]) #'set' object is not subscriptable

# HW :  find the meaning of  : subscriptable

# accessing the elements in a SET
s8 = {22,33,44,11,22,33,44,11}
print(s8)


# using for loop

for i in s8:
  print(i)

# Doubts in dictionary Methods
# update

d1= {
  'sameer' : 75,
  'saket': 89
}


d1.update({'sanket': 99})
print(d1)


# setdefault
# setdefault : get()  +  update()

print(d1.setdefault('sameer'))
print(d1.setdefault('suraj'))
print(d1)




# program 1 unique values 
setA = {11,22,33,44,33}
print(setA)

# # # program 2 set stores the value by index ??
# # #print(setA[0]) - No 

# # # program 3
setB = {"amol","satish","ram",22}
print(setB)

# # #program 4 # to verify a particular value in set
print("amol" in setB)

# # # program 5
print(len(setB))

# # # program 6
setC = {"pune","chandrapur","mumbai","pune"}

# # #        0         1       2        3
city = ["pune","nagpur","mumbai","banglore"]
print(type(city))
for x in range(4):
    #print(x)
    print(city[x])

for item in city:
    print(item)

for item in setC:
    print(item)

print(len(setC))


# # program 1

# # add()
setA = {11,22,33,44}
setA.add(333)
print(setA)

# # program 2 # clear()
setB = {"ram","satish","sachin","ramesh"}
setB.clear()
print(setB)


# # program 3 # pop() # remove(ele)
setB = {"ram","satish","sachin","ramesh"}
setB.remove("sachin")
print(setB)
setB.pop()
print(setB)

# # program 4
setB = {"ram","satish","sachin","ramesh"}
setB.update(["chinmay","tamnay"])
setB.update(("sarika","pranali"))
print(setB)

# # program 5
setB = {"ram","satish","sachin","ramesh"}
setC = setB 
setC.remove("ram")
print(setC)
print(setB) 

setE = setB.copy()
setE.remove("ram")
print(setE)
print(setB)


# #program 6
setH = {11,22,33}
setJ = {44,55,66}
setK  = setH.union(setJ)
print(setK)

setL = {11,22,33}
setB = {44,55,33}
setQ  = setL.intersection(setB)
print(setQ)


# # program 1
setA = {11,22,33}
setB = {33,44,55}
setC = setA.union(setB)
print(setC)

# # program 2

setC = {11,22,33,44}
setD = {33,44,55}
# setE = setC.intersection(setD)
# print(setE)
setC.intersection_update(setD)
print(setC)


setL = {11,22,33,44}
setJ = {66,77,88,99,22,44}
setL.intersection_update(setJ)
print(setL)


# # program 3

setF = {11,22,33,44}
setB = {66,11,33,99}

#setG = setF.symmetric_difference(setB)
setF.symmetric_difference_update(setB)
print(setF)


setQ = {11,22,33}
setM = {44,55,22}

# setN = setQ.symmetric_difference(setM)
# print(setN)
setM.symmetric_difference_update(setQ)
print(setM)


# # program 4
setQ1 = {11,22,44}
setQ2 = {66,22,88}
# setW = setQ1.difference(setQ2)
# print(setW)
# print(setQ1)

setQ1.difference_update(setQ2)
print(setQ1)


# # program 5
setQ1 = {11,22,33}
setQ2 = {11,22,33,44}
e = setQ2.issuperset(setQ1)
f = setQ1.issuperset(setQ2)
print(e)
print(f)
x = setQ1.issubset(setQ2)
print(x)

# # program6

setA = {11,22,33,88}
setB = {77,88,99}
h = setA.isdisjoint(setB)
print(h)

setG = {11,22,33,44}
w = setG.discard(55)
print(w)
print(setG)



