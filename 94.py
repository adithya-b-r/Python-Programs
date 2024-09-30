from array import *
import random

num=array('i',[])
tryagain="true"

for i in range (0,5):
    x=random.randint(0,100)
    num.append(x)

print(num)


while tryagain!="false":
    pos=int(input("Enter a number from list : "))

    if pos in num:
        print(pos,"is in the position",num.index(pos))
        tryagain="false"
    else:
        print("Entered number",pos,"is not in list!")