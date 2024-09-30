file = open("Names.txt","a")
file.write("\n"+input("Enter a name : "))
file.close()

file = open("Names.txt","r")
print(file.read())
file.close()