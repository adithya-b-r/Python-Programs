temp=[]
add=int(input("How many books do you want to add to the list : "))

file = open("Books.csv","a")
for i in range (0,add):
    name = input("Enter name : ")
    author = input("Enter author name : ")
    year = input("Enter year of release : ")
    newRecord = name+", "+author+", "+year+"\n"
    temp=newRecord
    file.write(newRecord)
file.close()

searchauthor=input("Enter an author name to search : ")

file = open("Books.csv","r")
count = 0
for row in file:
    if searchauthor in row:
        print(row)
        count=1
file.close()

if count == 0:
    print("There are no books of author", searchauthor)