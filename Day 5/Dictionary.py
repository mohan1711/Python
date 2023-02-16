# ex1; Creating a dictonary
# mydi = {100:'x',200:'y',300:'z'}
# print(mydi) #{100: 'x', 200: 'y', 300: 'z'}
#
#
# ex2; Access items from dictionary
# Normal way
# mydi =  {
#     "Model":"i10",
#     "Engine":"BS6",
#     "Brand":"Hyundai"
# }
# # print(mydi["Model"])    #i10
# # print(mydi["BS6"])      #KeyError: 'BS6'
# # get() method
# print(mydi.get("Brand"))    #Hyundai
#
# ex3: Change values from the dictionary
# mydi =  {"Model":"i10","Engine":"BS6","year":2020}
# print(mydi)     #{'Model': 'i10', 'Engine': 'BS6', 'year': 2020}
# mydi["year"]=2023
# print(mydi)     #{'Model': 'i10', 'Engine': 'BS6', 'year': 2023}
#
# ex4: Reading values from the dictionary
# mydi =  {"Model":"i10","Engine":"BS6","year":2020}
# for i in mydi:
#     print(i)  # Returns only key
# for i in mydi:
#     print(mydi[i])    # Returns only values
#
# ### output
# Model
# Engine
# year
# i10
# BS6
# 2020
#
# ex5: Read both key and value
# mydi =  {"Model":"i10","Engine":"BS6","year":2020}
# for x,y in mydi.items():
#     print(x,y)
#
# # output
# Model i10
# Engine BS6
# year 2020
#
# ex 6: Check if the is available or not
# mydi ={"Model":"i10","Engine":"BS6","year":2020}
# print('Model' in mydi)  #True
# #### or
# if 'Engine' in mydi:
#     print('yes present')    #yes present
# else:
#     print('not found')
#
# ex 7: Find the number of items in the dictionary
# mydi ={"Model":"i10","Engine":"BS6","year":2020}
# print(len(mydi))        #3
#
# ex8: Change values from the dictionary
# mydi =  {"Model":"i10","Engine":"BS6","year":2020}
# print(mydi)     #{'Model': 'i10', 'Engine': 'BS6', 'year': 2020}
# mydi["state"]="KA"
# print(mydi)   #{'Model': 'i10', 'Engine': 'BS6', 'year': 2020, 'state': 'KA'}
#
# ex9: Deleting the values from the dictionary
# mydi = {'Model': 'i10', 'Engine': 'BS6', 'year': 2020, 'state': 'KA'}
# mydi.pop('Model')
# del mydi['year']
# print(mydi)     #{'Engine': 'BS6', 'state': 'KA'}
# mydi.clear()    #This will clear the values but empty dictionary will be present
# print(mydi)     #{}
# del mydi        # will delete the complete dictionary and give NameError
# print(mydi)     #NameError: name 'mydi' is not defined
#
# ex10: Copying dictionary
# Method 1:
# mydi1 = {'Model': 'i10', 'Engine': 'BS6', 'year': 2020, 'state': 'KA'}
# mydi2 = mydi1
# print(mydi2)    #{'Model': 'i10', 'Engine': 'BS6', 'year': 2020, 'state': 'KA'}
#
# Method 2 : copy()
# mydi1 = {'Model': 'i10', 'Engine': 'BS6', 'year': 2020, 'state': 'KA'}
# mydi2 = mydi1.copy()
# print(mydi2)    #{'Model': 'i10', 'Engine': 'BS6', 'year': 2020, 'state': 'KA'}
#
