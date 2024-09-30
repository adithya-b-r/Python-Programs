import csv
tmp = []
x = 0

start = int(input("Enter starting year : "))
end = int(input("Enter ending year : "))

file = list(csv.reader(open("Books.csv")))
#print(file)

for row in file:
    tmp.append(row)

for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(row)
    x = x + 1