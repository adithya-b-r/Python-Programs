import csv

file = open("Books.csv","r")

x = 0

for row in file:
    display = "Row : "+str(x)+" - "+row
    print(display)
    x=x+1