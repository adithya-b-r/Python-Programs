n = int(input("Enter the number of elements in the list : "))
mylist = []
unique_list = []

for i in range(n):
    mylist.append(input(f"Enter element {i+1} : "))

for element in mylist:
    if mylist.count(element) == 1:
        unique_list.append(element)

print("Original list : ", mylist)
print("Unique list : ", unique_list)
