from array import *

nums = array ('i',[])

for i in range(1,6):
    i = str(i)
    nums.append(int(input("Enter number "+i+" : ")))

nums = sorted(nums)
print(nums)

getrid = int(input("Enter a number to remove from above array : "))
nums.remove(getrid)

print(nums)