# regular expression  - used on string - trying to find pattern of data

# \w - [a-z] [A-Z] [0-9]
# \W - [special symbols/char] non alpha-numeric
# \b - blank space
# \d - [0-9]
# \D - not[0-9]
# \A - match only at start of the string
# \Z - match only at end of the string

# need to import re (regular expression)

# search() - first occourance
# findall() - all occourance
# mathc() - start of the string
# spilt() - separate/split
# sub() - substitute - replace
# group() -

# program 1
# find pattern that start with m and followed by two char
# search() - find 1st occurance
import re
str = "map sun mop run"
result = re.search(r'm\w\w',str)
# print(result.group())
if result:
    print(result.group())


# program 2
# find pattern that matches all the occurance start with m and followed by two char
# findall() - find all occurance

str2 = "man ran sun fun map rap shape mate fate"
list2 = re.findall(r'm\w\w',str2)
# list2 = re.findall(r'm[\w]*',str2)  * is for followed by one or more char
print(list2)


# program 3
# match() - find at start of the string

str2 = "python is good language to learn"
q3 = re.match(r'p\w\w',str2)
# print(q3.group())
if q3:
    q3.group()


# program 4
# split() \W split at non-alphanumeric char

import re
str3 = "this : is the ; 'core' python's class"
# result = re.split(r'\W',str3)
result = re.split(r'\W+',str3)
print(result)

# program 5
# sub() - replace
str4 = "I am learning javascript"
q4 = re.sub(r'javascript','python',str4)
print(q4)

# program 6

import re
str = "the meeting will be conducted on 1st and 21st of this month"
# 1st 21st

# \d - for digit
result = re.findall(r'\b\d[\w]*',str)
# result = re.findall(r'\b\d[\d]*',str)
print(result)


# program 7

str = "one two three four five six seven 8 9 10"
# three seven [words has len of 5 = {5}]

list = re.findall(r'\b\w{5}',str)
print(list)

list = re.search(r'\b\w{5}',str)
print(list.group())

# list = re.match(r'\b\w{5}',str)
# print(list)  = as match find at start of string so o/p is none


list = re.findall(r'\b\w{4,}\b',str)
print(list)

list = re.findall(r'\b\w{3,5}',str)
print(list)

list = re.findall(r'\b\w{1,}',str)
print(list)

str = " one two three four five six seven 8 9 10 two"
list = re.findall(r't[\w]*\Z',str)
print(list)


str = "three one two three four five six seven 8 9 10 two"
list = re.findall(r'\At[\w]*',str)
print(list)