
numbers = [1,2,3,4,5]

# map ==> want to do operation with each element

# program 1 add 5 with each element of the list

e = lambda x:x+5   
# defined a lambda function to add 5 with each element
e2 = list(map(e,numbers))
# map used and wraped by list to get list as o/p
print(e2)

ue = list(map(lambda x : x+5 , numbers))
# used direct lambda function in place of e 
print(ue)

# e = lambda x:x + 5
# # ue = list(map(e,numbers))
# # print(ue)
# e2 = list(map(lambda x:x+ 5, numbers))
# print(e2)

# program 2  calculate age from birthyear

birthYear = [1989,1990,1991,1992]
#[35,34,33,32]

e3 = list(map(lambda x:2024-x,birthYear))
print(e3)

# with list comprehension
e4 = [2024-i for i in birthYear]
print(e4)

# e3 = list(map(lambda x : 2024 - x,birthYear))
# print(e3)
# e4 = [2024 - x for x in birthYear]
# print(e4)

# filter  ==>  to filter out element
# separate element for deposite and for withdrawl

transactions = [55,-66,33,-44,55,-66,77]

deposite = list(filter(lambda x:x>0,transactions))

withdrawl = list(filter(lambda x:x<0,transactions))

print(deposite)
print(withdrawl)

# with list comprehension

deposite = [i for i in transactions if i >0]
print(deposite)

withdrawl = [i for i in transactions if i<0]
print(withdrawl)

# deposit = [x for x in transactions if x > 0]
# withdrawl = [x for x in transactions if x < 0]
# print(deposit)
# print(withdrawl)
# e5 = list(filter(lambda x : x > 0 , transactions))
# print(e5)
# e6 = list(filter(lambda x : x < 0 , transactions))
# print(e6)


# separate marks above 70

marks  = [99,77,66,55,90,88,22,33,44]

e7 = list(filter(lambda x:x>70,marks))
print(e7)

above70 = [i for i in marks if i > 70]
print(above70)

# e7 = list(filter(lambda x : x > 70,marks))
# print(e7)

# reduce  ==> reduce elements in one single element

# from functools import reduce
# # need to import reduce from functools

lista = [11,22,33]
from functools import reduce
e = reduce(lambda acc,e1:acc+e1,lista,5)
# add 5 with element and add all, here acc is 5
# no need to wrap with list because o/p is one single element
print(e)

e = reduce(lambda acc,el:acc+el,lista,5)
print(e)