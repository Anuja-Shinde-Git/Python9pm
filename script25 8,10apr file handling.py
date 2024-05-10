# progeam 1 

# read , write , append

# file writing 

# # opening the file
# f = open('myfile2.txt','w')
# # taking input from the user
# name = input('enter the name')
# # writing to the file
# f.write(name)
# # closing the file
# f.close()


# # program 2

# file reading

# filename = input('Enter the file name')
# f= open(filename,'r')
# str = f.read()
# print(str)
# f.close()


# program 3

# file reading and filenotfound exception handling

# f = None
# try:
#     filename = input('Enter the file name')
#     f = open(filename,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print('file not found')
# finally:
#      if f is not None:
#       f.close        

# if file is blank then print file is blank

# f = None
# try:
#    filename = input('Enter file name')
#    f = open(filename,'r')
#    str = f.read()
#    if len(str) == 0:
#       print('file is blank')
#    else:  
#      print(str)
# except FileNotFoundError:
#    print('file not found')
# finally:
#    if f is not None:
#       f.close()


# program 4

# adding data to a file untill @ input
# \n to add new line

# f = open('myfile3.txt','w')
# while str != '@':
#   str = input('enter the names')
#   f.write(str)
# f.close()  


# but problem in above code that is each name should be in new line and @ should not print

# f = open('myfile3.txt','w')
# while str != '@':
#  str = input('enter the names')
#  if str != '@':
#       f.write(str + '\n')
# f.close()      


# program 5

# append a+ >> writting to the already existing file

# f = open('myfile2.txt','a+')
# while str != '@':
#     str = input("Enter the names ")
#     if str != '@':
#         f.write(str + '\n')
# str2 = f.read()
# print(str2)
# f.close()

# In this program read operation is not happened because while wrtting to the file cursor is at the end from the end there is no data
# in file so that we cant see anything in read mood 
# we use method 
# seek(0,0) >> start of the file
# seek(0,1) >> current position of the file
# seek(0,2) >> end of the file


# f = open('myfile2.txt','a+')
# while str != '@':
#     str = input('Enter the names')
#     if str != '@':
#         f.write(str + '\n')
# f.seek(0,0)        
# str2 = f.read()
# print(str2)
# f.close()        


# program 6

# checking for the file in system we use  module of python 'os' and 'sys' module
# if file is in sys then open if file is not available then exit

# import os ,sys

# fname =input('Enter the filename: ')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     sys.exit()   
# print('The file contains are: ') 
# str = f.read()
# print(str)
# f.close()   


# program 7

# open file myfile3.txt and count the no of lines , words and characters in it

# import os , sys

# fname = input('Enter filename: ')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     print('file does not exixts')
#     sys.exit()    

# cc = 0
# cw = 0 
# cl = 0

# for line in f:
#     # print(line)
#     cl = cl + 1

#     list = line.split()
#     cw = cw + len(list)

#     cc = cc + len(line)

# print(cl)
# print(cw)
# print(cc)    

# f.close()



# practice


# f = open('myfile2.txt','a+')
# while str != '@':
#     str = input('Enter the names')
#     if str != '@':
#       f.write(str + '\n')
# f.seek(0,0)      
# str2 = f.read()
# print(str2)      
# f.close()    

# checking if the file is in sys or not if is in then read it if not then exit

# import os , sys

# fname = input("Enter filename: ")
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     sys.exit()
# str = f.read()
# print(str)
# f.close        


# checking if the file is in sys or not if is in then append and read it if not then exit

# import os , sys
# fname = input('Enter the file name: ')
# if os.path.isfile(fname):

#     f = open(fname,'a+')
# else:
#     sys.exit()
# names = input('Enter the names: ')    
# f.write(names + '\n')
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close        


# import os , sys
# fname = input('Enter the file name: ')
# if os.path.isfile(fname):
#     f = open(fname,'a+')
#     while str != '@':
#         str = input('enter the names: ')
#         if str != '@':
#             f.write(str + '\n')
# else:
#     sys.exit()
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close  


import os , sys
fname = input('Enter the filename: ')
if os.path.isfile(fname):
    f = open(fname,'r')
else:
    sys.exit()
# str = f.read()
# print(str)

cl = 0
cw = 0
cc = 0

for line in f:
    cl = cl +1

    list = line.split()
    cw = cw + len(list)

    cc = cc + len(line)

print(cl)
print(cw)
print(cc)

f.close()

# import os , sys

# fname = input('Enter filename: ')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     print('file does not exixts')
#     sys.exit()    

# cc = 0
# cw = 0 
# cl = 0

# for line in f:
#     # print(line)
#     cl = cl + 1

#     list = line.split()
#     cw = cw + len(list)

#     cc = cc + len(line)

# print(cl)
# print(cw)
# print(cc)    

# f.close()