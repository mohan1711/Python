# EX 1 Creating of Tuple
# mytuple=("pig","ox","cow","deer","dog","cat")
# print(mytuple)      #('pig', 'ox', 'cow', 'deer', 'dog', 'cat')
#
# EX 2 Access the Tuple items
# mytuple=("pig","ox","cow","deer","dog","cat")
# print(mytuple[0])   #pig
# print(mytuple[1])   #ox
#
# EX 3 Access all tuple items
# mytuple=("pig","ox","cow","deer","dog","cat")
# for i in mytuple:
#     print(i)
#
# EX 4 Access tuple using range indexes
# mytuple=("pig","ox","cow","deer","dog","cat")
# print(mytuple[-4:-2])   #('cow', 'deer')
#
# EX 5: Change the tuple values
# But directly we cannot modify the values in the tuple since it is immutable
# But there is a work round -->tuple()-->list(modify)-->tuple()
#
# mytuple=("pig","ox","cow","deer","dog","cat")
# mylist = list(mytuple)
# print(mylist)   #['pig', 'ox', 'cow', 'deer', 'dog', 'cat']
# mylist[0] = "lion"
# mylist[5] = "tiger"
# mytuple=tuple(mylist)
# print(mytuple)  #('lion', 'ox', 'cow', 'deer', 'dog', 'tiger')
#
#
# EX 6: Search for an item in  the list
# mytuple = ("pig", "ox", "cow", "deer", "dog", "cat")
# if "pig" in mytuple:
#     print("YES")    #YES
# else:
#     print("NO")
#
# EX 7: Tuple length
# mytuple = ("pig", "ox", "cow", "deer", "dog", "cat")
# print(len(mytuple)) #6
#
# EX 8: Add items into the tuple
# mytuple = ("pig", "ox", "cow", "deer", "dog", "cat")
# mytuple[0] = "lion"     #TypeError: 'tuple' object does not support item assignment
# print(mytuple)
#
# EX 9: Copying of tuple
# mytuple1 = ("pig", "ox", "cow", "deer", "dog", "cat")
# mytuple2=mytuple1
# print(mytuple2) #('pig', 'ox', 'cow', 'deer', 'dog', 'cat')
#
# EX 10: Removing of the tuple - not possible due to immutable
# mytuple = ("pig", "ox", "cow", "deer", "dog", "cat")
# mytuple.remove("pig")   #Invalid - AttributeError: 'tuple' object has no attribute 'remove'
# del mytuple
# print(mytuple)  #NameError: name 'mytuple' is not defined. Did you mean: 'tuple'?
#
# EX 11: Join or Combine tuple
# tuple1 = (1,2,3)
# tuple2 = ("a","b","c")
# tuple3 = tuple1+tuple2
# print(tuple3)       #(1, 2, 3, 'a', 'b', 'c')
#
# # EX 12: Compare tuple equality
# m1 = (1,2,3)
# m2 = (1,2,3)
# if m1 == m2:
#     print('tuple are equal')     #list are equal
# else:
#     print('tuple not equal')
#
# # EX 13: