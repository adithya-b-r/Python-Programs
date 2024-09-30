list={}

for i in range (0,4):
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    shoe_size=int(input("Enter shoe size : "))
    list[name]={"Age":age,"Shoe size":shoe_size}
    print("\n")

for name in list:
    print((name),list[name]["Age"],list[name]["Shoe size"])

rm=input("Enter a name to remove : ")

del list[rm]

for name in list:
    print((name),list[name]["Age"],list[name]["Shoe size"])
