import csv

print("")
#file = open("Stars.csv","w")
#newRecord="Brian,73,Taurus\n"
#file.write(str(newRecord))
#file.close()

#file = open("Stars.csv","a")
#name = input("Enter name : ")
#age = input("Age : ")
#star = input("Enter star sign : ")
#newRecord = name+","+age+","+star+"\n"
#file.write(str(newRecord))
#file.close()

#file = open("Stars.csv","r")
#for row in file:
#   print(row)

file = open("Stars.csv","r")
reader = csv.reader(file)
print(reader)
rows=list(reader)
print(rows)
print(rows[1])