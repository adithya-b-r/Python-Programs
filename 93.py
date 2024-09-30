from array import *

num=array('i',[])

for i in range(0,5):
    x=int(input("Enter a number : "))
    num.append(x)

num=sorted(num)

print(num)

rm=int(input("Enter a number from list to remove : "))

num.remove(rm)

print(num)