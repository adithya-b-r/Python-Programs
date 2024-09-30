import csv

file = open("Books.csv","r")
rnum = 1

for row in file:
    print("["+str(rnum)+"]",row)
    rnum = rnum + 1

file.close()