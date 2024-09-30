from array import *
nums = array ('i',[12, 15, 89, 13, 12])

print(nums)
num = input("Enter a number from above array : ")
num = int(num)

print("The number",num,"has repeated",nums.count(num),"times!")