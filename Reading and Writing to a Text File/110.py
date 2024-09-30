file = open("Names.txt","r")
print(file.read())
file.close()

remove = input("Enter a name to remove : ")

file = open("Names.txt","r")

for name in file:
    if name != remove:
        file = open("Names2.txt","a")
        file.write(name)
        file.close()

file.close()