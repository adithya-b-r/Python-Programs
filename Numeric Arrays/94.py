from random import randint
from array import *

nums = array ('i',[86,366,525,1000,323])
user = True

print(nums)
ask = int(input("Enter a number from above array : "))

while user == True:
    if ask in nums:
        print(nums.index(ask))
        user = False
    else:
        ask = int(input("Try again : "))