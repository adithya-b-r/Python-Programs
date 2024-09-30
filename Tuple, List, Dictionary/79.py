nums = []

for i in range(1,4):
    i = str(i)
    num = int(input("Enter number "+i+" : "))
    nums.append(num)

last_num = input("Do you want to keep the last number [y/n] : ")

if last_num == 'n':
    nums.pop()

print(nums)