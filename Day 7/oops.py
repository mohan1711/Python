#Example 1:

#class first():
#    def dummy(self): #Self denotes that this method belongs to the particular class - Its Mandatory
#        pass            #Pass must be specified in a method is not returning or printing anything.
#    def name(self):
#        print("john")
#    def display(self, age ):
#        print('age of john is', age )

#obj=first()         #-----> This is how we create the object.
#obj.dummy()         # doesnt return anything so no o/p
#obj.name()          #john is o/p
##obj.display()      #TypeError: first.display() missing 1 required positional argument: 'age'
#obj.display(25)     #age of john is 25


#Example 2:

#class abc():
#    def meth(self):
#        print('This is an instance method')
#    @staticmethod
#   def stat(num):
#        print(num)

#obj=abc()
#obj.meth()  #This is an instance method

#abc.stat(100)   #100 ----> static methods can be called directly using the class not through object.


#Example 3: class variables

#class myclass():
#    a,b=10,20  #**** class variables
#    def add(self):
#        print(self.a+self.b) #class variables can be invoked using self keyword
#    def mul(self):
#        print(self.a*self.b)

#obj=myclass()
#obj.add()   #30
#obj.mul()   #200

#Example 4: global,local and class variables
#i,j = 20, 30    #global variables - accessed every where
#class myclass():
#    x,y = 5, 15     #class variables - within the class
#    def add(self,a,b):  #local variables - within the method
#        print(a+b)              #3
#        print(self.x+self.y)    #20
#        print(i+j)              #50
#obj=myclass()
#obj.add(1,2)    #passed value to the local variables



#Example 5: same as above ex but with same variable name a,b in g,l,c variables

#a,b = 20, 30    #global variables - accessed every where
#class myclass():
#    a,b = 5, 15     #class variables - within the class
#    def add(self,a,b):  #local variables - within the method
#        print(a+b)              #3
#        print(self.a+self.b)    #20
#        print(globals()['a']+globals()['b']) #50
#obj=myclass()
#obj.add(1,2)    #passed value to the local variables

#Example 6: Once class with multiple objects

#class myclass():
#    def display(self,name):
#        print('My name is',name)
#o1 = myclass()
#o1.display('Dave')  #My name is Dave


#o2 = myclass()
#o2.display('John')  #My name is John


#Example 7: Constructor example

#class myclass:
#    def __init__(self):     # This is a constructor
#        print('This is a constructor')
#    def show(self):
#        print('This is a method')
#obj=myclass()   #Invokes constructor automatically #o/p This is a constructor
#obj.show()      #To be called explicit thru an object #o/p This is a method 

























        


















