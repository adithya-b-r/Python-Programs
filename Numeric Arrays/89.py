from array import *
from random import randint as ranint

nums = array ('i',[])

for i in range(0,5):
    nums.append(ranint(0,1000))

for i in nums:
    print(i)