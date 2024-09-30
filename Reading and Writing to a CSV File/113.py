import csv
count = 0

record = input("How many records do you want to add to the list : ")
record = int(record)

file = open("Books.csv","a")

for i in range(0,record):
    book = input("Book name : ")
    author = input("Author name : ")
    r_year = input("Year released : ")
    file.write("\n"+book+", "+author+", "+r_year)

file.close()

auth_name = input("Enter a author name : ")

file = open("Books.csv","r")

for row in file:
    if auth_name in str(row):
        print(row)
        count = 1

if count == 0:
    print("No record of author",auth_name)

file.close()