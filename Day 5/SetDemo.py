# EX 1: Creating the set
# myset = {'ganga','kaveri','yamuna'}
# print(myset)    #{'yamuna', 'ganga', 'kaveri'}
#
# EX 2: Access all itesm from set
# myset = {'aa','bb','cc,'}
# for i in myset:
#     print(i)
#
# EX 3: Value exists in set or not
# myset = {'app','ball','cat'}
# print('app' in myset)   #True
# print('bal' in myset)   #False
#
# EX 4: adding items in set - add()-for single item or update() for multiple item
#
# using add()
# myset = {'app','ball','cat'}
# myset.add('dog')
# print(myset)    #{'ball', 'app', 'dog', 'cat'}
#
# using update()
# myset = {'app','ball','cat'}
# myset.update(['pig','deer'])
# print(myset)    #{'deer', 'ball', 'cat', 'pig', 'app'}
#
#
# EX 5: Find number of items in a set
# myset = {'app','ball','cat'}
# print(len(myset))   #3
#
# EX 6: Remove item from the set
# Method 1 using remove()
# myset = {'app','ball','cat'}
# myset.remove('cat')
# print(myset)    #{'ball', 'app'}
# myset.remove('abc')     #KeyError: 'abc'
#
# Method 2 using discard()
# myset = {'app','ball','cat'}
# myset.discard('cat')
# print(myset)    #{'ball', 'app'}
# myset.discard('abc')  #Doesnt give any error
#
# EX 7: Remove all elements from set
# Using clear()
# myset = {'app','ball','cat'}
# myset.clear()
# print(myset) #set()
#
# Using del()
# myset = {'app','ball','cat'}
# del myset
# print(myset) #set()
#
# EX 7: Joining two set using union() or update()
# using union()
# s1 = {'abc','xyz'}
# s2 = {1,2}
# s3 = s2.union(s1)
# print(s3)   #{1, 2, 'xyz', 'abc'}
#
# using update()
# s1 = {'abc','xyz'}
# s2 = {1,2}
# s2.update(s1)
# print(s2)   #{1, 2, 'xyz', 'abc'}
#
