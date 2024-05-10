# file handling

# read >> 'r' >>  read the file 
# write >> 'w' >> write the file
# append >> 'a+' >> add to a existing file

# Never forget to close the file at any situation
# if we want to read a file if there is file then it will read and if there is no file the it will create and then read

# open is inbuilt class and creating object of that class

# # creation of object
# f = open('myfile.txt','w')
# # taking user input
# str = input('Enter the name')
# # writing to the file
# f.write(str)
# # closing the file
# f.close()

# reading the existing file

# file_name = input('Enter the file name')
# f= open(file_name,'r')
# str = f.read()
# print(str)
# f.close()

# trying to open file that is not existing and hadleing the exception

# f = None
# try:
#     fileName = input('Enter the file Name')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)

# except FileNotFoundError:
#     print('File not found')    
    
# finally:
    
#     if f is not None:
#         f.close()    



# f = None
# try:
#  fileName = input("Enter file name")
#  f = open(fileName,'r') 
#  str = f.read()
#  print(str)
# except FileNotFoundError:
#    print('file not found')
# finally:
#    if f is not None:
#       f.close()
#    else:
#       print('blank file')  
      

  
  
    