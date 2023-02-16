#Constructor with an argument expected

#Example 1:
#class myconc():
#    name = 'Ram'
#    def __init__(self,name):    #constructor expect an argument
#        print('The name inside the constructor is',name)    #The name inside the constructor is Krishna
#        print('The name from class variable is',self.name)  #The name from class variable is Ram
#obj = myconc('Krishna') #argument passed to constructor

#Example 2: Class variables inside a constructor
#REQ: EMP #Constructor - ename,eid,sal #Method - display() : print eid,ename,sal

#class myclass():
#    def __init__(self,eid,ename,sal):
#        self.eid = eid  #Declaring class variables inside a constructor
#        self.ename = ename
#        self.sal = sal
#    def display(self):
#        print(self.eid,self.ename,self.sal) #Calling class variables 
#emp1=myclass(11,'ram',25000)
#emp1.display()       #11 Ram 25000
#
#emp2=myclass(22,'kalki',30000)
#emp2.display()     #22 kalki 30000


#Example 3: EMP Constructor: ename,eid and also display them using constructor

class myclass():
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename
    def __str__(self):      #__str__ returns only strings. Here its not useful
        print(self.eid,self.ename)
obj=myclass(10,'mohan')
print(obj)  #10 mohan   __str__ returned non-string (type NoneType)














        

