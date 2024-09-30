from array import *
import random

num1=array('i',[])
num2=array('i',[])

for i in range (0,5):
    x=random.randint(0,100)
    num1.append(x)

for i in range (0,3):
    x=int(input("Enter a number : "))
    num2.append(x)

num1.extend(num2)

num1=sorted(num1)

for i in num1:
    print(i)