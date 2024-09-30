list={}

for i in range (0,4):
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    shoe_size=int(input("Enter shoe size : "))
    list[name]={"Age":age,"Shoe size":shoe_size}
    print("\n")

print(list)