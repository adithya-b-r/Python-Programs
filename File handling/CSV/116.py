import csv

file = list(csv.reader(open("Books.csv")))

tmp = []

for row in file:
    tmp.append(row)

x = 0
for row in file:
    display = str(x) + str(row)
    print(display)
    x=x+1

select = int(input("Select a row to remove : "))
del tmp[select]

x = 0
for row in tmp:
    display = str(x) +" "+ str(tmp[x])
    print(display)
    x = x + 1

change = int(input("Enter a row to change : "))

x=0
for row in tmp[change]:
    display = str(x) +" "+ str(tmp[change][x])
    print(display)
    x = x+1

part = int(input("Which part do you want to change : "))
newData = input("Enter new data : ")

tmp[change][part] = newData
print(tmp[change])

file = open("Books.csv","w")
x = 0
for row in tmp:
    newRecord = tmp[x][0]+", "+tmp[x][1]+", "+tmp[x][2]+"\n"
    file.write(newRecord)
    x = x + 1

file.close()