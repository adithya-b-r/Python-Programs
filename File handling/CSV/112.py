file = open("Books.csv","r")
print(file.read())
file.close()

file = open("Books.csv","a")
name = input("Enter book name : ")
author = input("Enter author name : ")
year = input("Enter year of released : ")

newRecord = name+", "+author+", "+year+"\n"
file.write(newRecord)
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()