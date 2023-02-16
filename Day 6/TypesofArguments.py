# Example 1:

#Positional arguments
# def num(a,b):
#     print(a,b)
# #num()   #TypeError: num() missing 2 required positional arguments: 'a' and 'b'
# num(10,20)  #10 20 - Positional arguments
# num(a=20,b=10)  #20 10 - Keyword arguments

# EX 2: Default values assigned to positional arguments
# def num(i,j=10):
#     print(i,j)
# num(100)    #o/p is  100 10
# num(100,200)    #o/p is 100 200

# EX 3: Keyword arguments
# def key(name,greet):
#     print(greet+" "+name)
# key(greet='Hi',name='Anu')  #Hi Anu - keyword
# key(name='Anu',greet='Hi')  #Hi Anu - keyword
# key('Hi','Anu') #Anu Hi - Positional

# EX 4: Combination of position and keyword arguments
# *** position argument must appear before any keyword arguments
#
# def fun(a,b,c):
#     print(a,b,c)
# fun(10,20,30)   # 10 20 30
# fun(a=10,b=20,c=30) # 10 20 30
# fun(c=30,a=10,b=20) # 10 20 30
# fun(10,20,c=30) # 10 20 30
# fun(10,c=30,b=20)   # 10 20 30
# fun(a=10,20,30)  # Error - positional argument is found after keyword argument ***


# Example 5: A function can return multiple values
def large(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(large(100,200))       #(200,100)  Tuple
print(large(30,10))         #(30,10) Tuple







