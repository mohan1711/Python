#INHERITANCE - Acquiring all the variables and methods from one class to another class.

# class A ---> x,y,z m1()   *A is parent of child B     *Also called super or base class
# class B ---> a,b,c m2() m3() *B is child  of A class  * Also called derived or sub class

# OBJECTIVES: Code re-usability and avoiding duplication

# TYPES of Inheritance
# 1. Single - one parent and one child
# 2. Mutlilevel - child1<------child2<---------child3<--------child4
# 3. Hierarchical - one parent class --- many child class extends to parent but child classes doesnt interact each other.
# 4. Mutliple - Many parent class with one child class but parents doesnt interact with each other.

#Example 1: Single I

#class A:
#    def ma(self):
#        print('This is method of class A')
#class B(A): #Inheriting parent class A through child class B
#    def mb(self):
#        print('This is method of class B')
#        
#objB=B()
#objB.mb()   #This is method of class B
#objB.ma()   #THis is method of class A

#Example 2: Single I

#class A:
#    a,b = 10,20
#    def add(self):
#        print(self.a+self.b)
#class B(A):
#    x,y = 200,100
#    def sub(self):
#        print(self.x-self.y)
#
#Bobj = B()
#Bobj.sub()  #100
#Bobj.add()  #30

#Example 3: Multilevel I
#class A:
#    a,b = 10,20
#    def add(self):
#        print(self.a+self.b)
#class B(A):
#    x,y = 200,100
#    def sub(self):
#        print(self.x-self.y)
#class C(B):
#    i,j = 2,5
#    def mul(self):
#        print(self.i*self.j)
#
#cobj=C()
#cobj.add()  #30
#cobj.sub()  #100
#cobj.mul()  #10

#Example 4: Hierarchy I

#class A:
#    a,b = 10,20
#    def add(self):
#        print(self.a+self.b)
#class B(A):
#    x,y = 200,100
#    def sub(self):
#        print(self.x-self.y)
#class C(A):
#    i,j = 2,5
#    def mul(self):
#        print(self.i*self.j)
#
#bobj=B()
#bobj.sub()  #100
#bobj.add()  #30
#
#cobj=C()
#cobj.mul()  #10
#cobj.add()  #30

#Example 5: Multiple I

#class P1:
#    def m1(self,a,b):
#        print(a+b)
#class P2:
#    def m2(self,x,y):
#        print(x*y)
#class C(P1,P2):        #Two parents with one child class, child extends to p1 and p2 but p1 and p2 are not linked.
#    def m3(self,i,j):
#        print(i-j)

#Cobj = C()
#Cobj.m1(10,20)  #30
#Cobj.m2(2,10)   #20
#Cobj.m3(100,50) #50


#Example 6: Based on overriding and super class(calling method of child class using super keyword)

#class A:
#    def m1(self):
#        print('This is m1 method from class A')
#class B(A):
#    def m1(self):
#        print('This is m1 method from class B')
#        super().m1()
#
#bobj=B()        
#bobj.m1()   #This is m1 method from class B
            ##This is m1 method from class A

#Example 7:

#class A:
#    x,y = 10,20
#
#class B(A):
#    i,j = 20,40
#    def add(self,a,b):
#        print(a+b)
#        print(self.i+self.j)
#        print(self.x+self.y)
#
#bobj=B()
#bobj.add(1,2)   #3
                #60
                #30


# Example 8: Over riding variables

#class Parent:
#    name = 'John'
#class Child(Parent):
#    name = 'Scott'
#    def meth(self):
#        print(super().name)
#
#cobj=Child()
#print(cobj.name)    #Scott
#cobj.meth()         #John

#Example 9: Overriding methods


#class Bank():
#    def intrate(self):
#        return 0
#class SBI(Bank):
#    def intrate(self):
#        return 13
#class IOB(Bank):
#    def intrate(self):
#        return 15

#o_sbi=SBI()
#print(o_sbi.intrate())      #13
#o_iob=IOB()
#print(o_iob.intrate())      #15

#Example 10: POLYMORPHISM: Achieved using overloading concept
#**** Overloading 1
#Poly: One in many form

#class Human:
#    def say(self,name=None):
#        if name is not None:
#            print('hello',name)
#        else:
#            print('hello')
#obj = Human()
#obj.say()   #hello
#obj.say('Mohan')    #hello Mohan

# ******** Overloading 2

#class Calc:
#    def ops(self,a=0,b=0,c=0):
#        print(a+b+c)

#obj = Calc()
#obj.ops()       #0
#obj.ops(10,20)  #30
#obj.ops(10,20,30)   #60
























