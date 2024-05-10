import pickle
class Emp:
    def _init_(self,fn,ln,salary):
        self.firstName = fn 
        self.lastName = ln
        self.salary = salary

    def displayInfo(self):
        print(self.firstName)
        print(self.lastName)
        print(self.salary) 

# f = open('emp.dat', "wb")
# users  = int(input('Enter the number of users:')) #"3" ---- 3

# for i in range(users):
#     fn = input("Enter the firstName")
#     ln = input("Enter the lastName")
#     salary = int(input("Enter the salary"))
#     e = Emp(fn,ln,salary)
#     pickle.dump(e,f)

# f.close()
# f = open('emp.dat',"rb")
# while True:
#     try:
#         e =  pickle.load(f)
#         e.displayInfo()
#     except EOFError:
#         print("EOF file reached")
#         break
# f.close()