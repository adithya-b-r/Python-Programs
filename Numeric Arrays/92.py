from array import *
from random import randint

array1 = array ('i',[])
array2 = array ('i',[])

for i in range(0,5):
    array2.append(randint(1,1000))

for i in range(1,4):
    i = str(i)
    array1.append(int(input("Enter number "+i+" :")))

array1.extend(array2)

print(array1)