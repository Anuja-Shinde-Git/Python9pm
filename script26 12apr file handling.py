# Image file

# image file is binary file 'b' >> to open file need open in 'rb' read binary mode

# want to read image file and write it in other file



# program 1 

# # open file image file in read mode
# rb = open ('hitman.jpg','rb')
# # open/create another file in write mode
# rb2 = open('hitman2.jpg','wb')
# # read data from image file
# bytes = rb.read()
# # write data in another file
# rb2.write(bytes)
# # close both the files
# rb.close()
# rb2.close()


# program 2

# India = open('ICC India.jpg','rb')
# India2 = open('ICC2 India.jpg','wb')
# bytes = India.read()
# India2.write(bytes)
# India.close()
# India2.close()



# we can handle files with 'with' also, you need to no worry about file closing 'with' take care of it , just need to give alias to the file

# with open('info4.txt','w') as f:
#     f.write('I am learning js'+'\n')
#     f.write('I am learning python')

# with open("info4.txt",'r') as f2:
#     str = f2.read()
#     print(str)



# we can add the python object into data file using dump method called pickle >> dump method convert object into data file
# and also we can add data file into python object using load method called unpickle >> load method convert data file into object
# pickle is inbuilt class in python and we need to import it 
# dump >> file extention .dat

# python object -----> data file write
# data file read ----> python object -----> display details

# import pickle
# class Emp:
#     def __init__(self,fn,ln,email,age):
#         self.firstname = fn
#         self.lastname = ln
#         self.email = email
#         self.age = age

#     def displayDetails(self):
#         print(self.firstname)
#         print(self.lastname)
#         print(self.email)
#         print(self.age) 

# # open the file where we need to store object's data file
# f = open('student.dat','wb')           

# # input from user for how many objects want to create
# n = input('Enter the number of objects: ')

# # loop will run n times as n no.of objects will create
# for x in range(n):
#     # taking input from user
#     fn =input('Enter firstname')
#     ln = input('Enter lastname')
#     email = input("Enter email")
#     age = input('Enter age')
#     # object creation
#     e = Emp(fn,ln,email,age)
#     # dumping object into data file
#     pickle.dump(e,f)

# f.close()    