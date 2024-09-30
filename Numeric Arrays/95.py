from array import *

nums = array ('f',[12.34,25.12,57.12,34.79,94.42])
tryagain = True
unum = int(input("Enter a number between [2 - 5] : "))

while tryagain == True:
    if unum>=2 and unum<=5:
        tryagain = False
    else:
        print("Out of range!")
        unum = int(input("Try again : "))
        

for num in nums:
    print(round(num/unum,2))