nums = [123,234,345,456]

for i in nums:
    print(i)

num = int(input("Enter a three digit number : "))

if num in nums:
    print(nums.index(num))
else:
    print("That is not in the list!")