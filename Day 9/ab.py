# Approach 1
# import a
# import b
#
# obj_a = a.Animal()
# obj_b = b.Bird()
# obj_a.fav()     #I like cow
# obj_b.fav()     #I like parrot

# Approach 2

from a import Animal
from b import Bird

obja = Animal()
obja.fav()      #I like cow

objb = Bird()
objb.fav()      #I like parrot