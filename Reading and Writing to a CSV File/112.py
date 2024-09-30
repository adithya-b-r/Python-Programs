import csv

file = open("Books.csv","a")

book = input("Book name : ")
author = input("Author name : ")
r_year = input("Year released : ")

file.write("\n"+book+", "+author+", "+r_year)
file.close()