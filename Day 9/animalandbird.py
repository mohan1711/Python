#Approach 1

import animal
import bird

animal.fly()        #Animal cant fly
animal.color()      #Animal color is brown
bird.color()        #Bird color is green
bird.fly()          #Bird can fly


#Approach 2

from animal import *
animal.color()      #Animal color is brown
animal.fly()        #Animal cant fly
from bird import *
bird.fly()          #Bird can fly
bird.color()         #Bird color is green
