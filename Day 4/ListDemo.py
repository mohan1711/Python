# Example - How to create the list
#
# mylist1 = [10,20,30,40,50]
# mylist2 = ["java","python","ruby","C","php"]
# mylist3 = ["mohan",20,"babu",40]
# mylist4 = list()
#
# print(mylist1)  #[10, 20, 30, 40, 50]
# print(mylist2)  #['java', 'python', 'ruby', 'C', 'php']
# print(mylist3)  #['mohan', 20, 'babu', 40]
# print(mylist4)  #[]
#
# Accessing individual items from the list
# l = ["apple","cherry", "banana"]
# print(l[-1])  #banana
# print(l[0])   #apple
#
# Access using range of index
# l = ["apple","cherry", "banana", "berry", "grapes"]
# print(l[2:4]) #['banana', 'berry']
#
# Change the value from the list
# fruit = ['apple','banana','cherry']
# fruit[0]='guava'
# print(fruit)    #['guava', 'banana', 'cherry']
#
# Read the list items using for loop
# fruit = ['apple','banana','cherry']
# for i in fruit:
#     print(i)
#
# Check if item exists in the list or not
# fruit = ['apple','banana','cherry']
# if 'apple' in fruit:
#     print("Yes... found!!!")
# else:
#     print("No... Not found!!!")
#
# List length
# fruit = ['apple','banana','cherry']
# print(len(fruit)) #3
#
# Add new item in the list
# fruit = ['apple','banana','cherry']
# fruit.append('orange')
# print(fruit) #['apple', 'banana', 'cherry', 'orange']
#
# Add in between the list
# fruit = ['apple','banana','cherry']
# fruit.insert(2,'berry')
# print(fruit)    #['apple', 'banana', 'berry', 'cherry']
#
# Remove item from the list
#
# Method 1 - pop
# fruit = ['apple', 'banana', 'berry', 'cherry']
# fruit.pop(3)
# print(fruit)       #['apple', 'banana', 'berry']
#
# Method 2 - del
# fruit = ['apple', 'banana', 'berry', 'cherry']
# del fruit[1]
# print(fruit)    #['apple', 'berry', 'cherry']
#
# Method 3 - clear It removes all items from the list
# fruit = ['apple', 'banana', 'berry', 'cherry']
# fruit.clear()
# print(fruit)    #[]
#
# Copy from one list to another
#
# Method 1
# fruit = ['apple', 'banana', 'berry', 'cherry']
# new = list(fruit)
# print(new)      #['apple', 'banana', 'berry', 'cherry']
#
# Method 2
# fruit = ['apple', 'banana', 'berry', 'cherry']
# new = fruit.copy()
# print(new)      #['apple', 'banana', 'berry', 'cherry']
#
# Combine or Join the lists
# Method 1 - Using Concetation
# lista = ["abc","pqr","xyz"]
# listb = [1,2,3]
# listc = lista+listb
# print(listc)    #['abc', 'pqr', 'xyz', 1, 2, 3]
#
# Method 2 - Using looping statements
# lista = ["abc","pqr","xyz"]
# listb = [1,2,3]
# for i in listb:
#     lista.append(i)
# print(lista)    #['abc', 'pqr', 'xyz', 1, 2, 3]
#
# Method 3 - Using extend
# lista = ["abc","pqr","xyz"]
# listb = [1,2,3]
# lista.extend(listb)
# print(lista)    #['abc', 'pqr', 'xyz', 1, 2, 3]
#
# # Find equality of list
# m1 = [1,2,3]
# m2 = [1,2,3]
# if m1 == m2:
#     print('list are equal')     #list are equal
# else:
#     print('list not equal')
#
