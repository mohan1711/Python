# Example 1

# global_var = 20
#
# def fun():
#     local_var = 50
#     print(global_var)   #20
#     print(local_var)    #50
# fun()
#
# print(local_var)    #Invalid because the local_var is part of fun() i.e, local variable
# print(global_var)



# Example 2:
# ab = 100
# def func():
#     ab = 50   #local variable
#     print(ab)   #50
# func()



# Example 3: Using global variable in local variable and updating value
# ab = 100
# def func():
#     global ab
#     ab = 50 #global variable
#     print(ab)   #50
# func()



# Example 4:
# xy = 100
# def func():
#     global xy
#     xy = 50 #global variable
#     print(xy)   #50
# func()  #50
# print(xy)   #50



# Example 5:
# xy = 100
# def func():
#     global xy
#     xy = 50 #global variable
#     print(xy)   #50 if function is called
# ### func()
# print(xy)   #100



#   Example 6:
def cool():
    global x
    x=200
    print(x)
cool()  #50
print(x)    #50 - able to access because x is a global variable

# Global variables can be declared inside a function using global keyword
