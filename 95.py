from array import *
import math

num=array('f',[20.34,24.56,10.78,71.29,2.65])
tryagain="false"

while tryagain=="false":
    unum=int(input("Enter a number between [2-5] : "))

    if unum>=2 and unum<=5:
        tryagain="true"
    else:
        print("Out of range!")

for i in num:
    print(round((i/unum),2))