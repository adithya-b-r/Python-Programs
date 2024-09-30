from array import *

nums=array('i',[45, 324,654,45,264])
print(nums.count(45))
print(nums)

for x in nums:
    print(x)

nums.append(99)

print(nums)

nums.reverse()

nums.pop()

print(nums)