import random
from array import *

int_num=array('i',[])

for i in range (0,5):
    x=random.randint(0,100)
    int_num.append(x)

for i in int_num:
    print(i)
