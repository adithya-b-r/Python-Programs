from array import *

nums = array ('i',[])

for i in range(0,5):
    i = str(i)
    nums.append(int(input("Enter number "+i+" : ")))

nums = sorted(nums)
nums.reverse()

print(nums)