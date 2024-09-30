file = open("Names.txt","r")
print(file.read())
file.close()

file = open("Names.txt","a")
name=input("Enter a new name : ")
name="\n"+name
file.write(name)
file.close()

file = open("Names.txt","r")
print(file.read())
file.close()