import csv

file = list(csv.reader(open("Books.csv")))
temp = []
rnum = 1

for row in file:
    print(str(rnum)+".",row)
    rnum = rnum + 1

for row in file:
    temp.append(row)

getrid = int(input("Which row would you like to remove : "))
getrid = getrid - 1

del temp[getrid]

rnum = 1
for row in temp:
    print(str(rnum)+".",row)
    rnum = rnum + 1

alter = int(input("Enter a row number to alter : "))
alter = alter - 1

rnum = 1
for row in temp[alter]:
    print(str(rnum)+".",row)
    rnum = rnum + 1

change = int(input("Enter row number to change data : "))
change = change - 1

newRecord = input("Enter new data : ")

temp[alter][change] = newRecord

rnum = 1
for row in temp:
    print(str(rnum)+".",row)
    rnum = rnum + 1

print(temp[alter])

file = open("Books.csv","w")

rnum = 0
for row in temp:
    record = temp[rnum][0] +", "+ temp[rnum][1] +", "+ temp[rnum][2] + "\n"
    file.write(record)
    rnum = rnum + 1

file.close()