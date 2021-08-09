### Task[1]: creat new class ...... ###
class BankAccount:
    def __init__(self):
        self.Name = input("please Enter your name: ")
        self.__Password = input("please enter your password: ")
        self.Credit = 0
     
    def addCredit(self):
        newamout = float(input("please enter how much money you add: "))
        self.Credit+=newamout
    
    def showCredit(self):
        checkPass = input("please enter your password to continue: ")
        if (checkPass == self.__Password):
            print(self.Credit)
    
    def changePassword(self):
        checkPass = input("please enter your password to continue: ")
        if (checkPass == self.__Password):
            newPassword = input("please enter your new password: ")
            self.__Password = newPassword
            
    def addEmail(self):
        self.Email = input("please enter your email: ")  
        
    def getattributes(self):
        return self.Name, self.__Password, self.Credit, self.Email
    
 
attributes = ['Name: ', 'Password: ', 'Credit: ', 'Email: ']    
i = 0

clint = BankAccount()
clint.addCredit()
clint.addEmail()

f = open('Attributes.txt', 'w')

for attribute in clint.getattributes():
    f.write(attributes[i] + str(attribute) + '\n')
    i += 1
    
f.close()

print()
f = open('Attributes.txt', 'r')
print(f.read())
f.close()

print('#'*50, '\n')
##################################################

### Task[2]: Implement composition concept using python with 2 Classes ###
class Component:
	def __init__(self):
		print('Component class object created...')

	def m1(self):
		print('Component class --> m1() method executed...')


class Composite:
	def __init__(self):
		self.obj1 = Component()              # object from the Component Class	
		print('Composite class object also created...')

	def m2(self):
        # self.obj1.m1()
		print('Composite class --> m2() method executed...')
		self.obj1.m1()

obj2 = Composite()
obj2.m2()
