# Three Types
#
# 1. Conditional Statements
#         if if else elif
#
# 2. Looping Statements
#         while for
#
# 3. jumping statements
#         break   continue



# Example 1
# age = 20
# if age>=18: #After any condition colon shall be included
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


#Example 2

# if False:
#     print('Statement is True')
# else:
#     print('Statement is False')


#Example 3: Find the number is even or odd

# num = int(input('Enter a number'))
# if num%2==0:
#     print('The number is even')
# else:
#     print('The number is odd')


#Example 4 if else in single line (Ternary operator)

# num = 23
# print('even number') if num%2==0 else print('odd number')


#Example 5 if else if multiple statements to be printed (Ternary operator)

# num = 5
# {print('Hello'),print('Java')} if num%2==0 else {print('Hi'),print('Python')}


#Example 6 Multiple conditions then use elif condition

# wkno = int(input('Enter the week no'))
# if wkno==1:
#     print('Sunday')
# elif wkno==2:
#     print('Monday')
# elif wkno==3:
#     print('Tuesday')
# elif wkno==4:
#     print('Wednesday')
# elif wkno==5:
#     print('Thursday')
# elif wkno==6:
#     print('Friday')
# elif wkno==7:
#     print('Saturday')
# else:
#     print('Invalid weekday')


# Example 7 Check the largest of two numbers
# a,b=20,10
# print('a is greater') if a>b else print('b is greater')

#Example 7 Find Largest of three numbers

# a,b,c = 10,20,5
# if a>b and a>c:
#     print('a is greater')
# elif b>a and b>c:
#     print('b is greater')
# else:
#     print('c is greater')

#Example 8 Print the week number if you give weekday as the input


#Example 9 Check if the given number is +ve or -ve

num = int(input('Enter a number'))
if num==0:
    print('Number is zero')
elif num>0:
    print('Number is positive')
else:
    print('Number is negative')




