from array import *
nums = array ('i',[])
count = 0

while count <= 5:
    num = int(input("Enter a number between [10-20]: "))
    if num>=10 and num<=20:
        nums.append(num)
        count = count+1
    else:
        print("Out of range!")

print("Thank you!")

for num in nums:
    print(num)