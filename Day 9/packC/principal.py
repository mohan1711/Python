import sys
sys.path.append('C:/Users/com/PycharmProjects/pythonProject/Day 9/packA')
sys.path.append('C:/Users/com/PycharmProjects/pythonProject/Day 9/packB')


#Approach 1
# import emp
# import stu

# empobj=emp.employee(101,'john',35000)   #employee class cant directly import so emp.employee
# empobj.dispemp()        #101 john 35000
#
# stuobj =stu.student(55,'anu',10)
# stuobj.dispstu()    #55 anu 10

#Approach 2

from emp import *
from stu import *

empobj=employee(120,'scott',52000)
empobj.dispemp()        #120 scott 52000

stuobj=student(12,'ram',10)
stuobj.dispstu()        #12 ram 10









