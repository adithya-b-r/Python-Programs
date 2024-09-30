from array import *

num=array('i',[])

while len(num) < 5:
    x=int(input("Enter a number : "))

    if x>=10 and x<=20:
        num.append(x)
    else:
        print("Outside range!")

print("Thank you!")

for i in num:
    print(i)