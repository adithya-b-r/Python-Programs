from sqlite3 import Row


list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

row=int(input("Enter a row :"))
column=int(input("Enter a column :"))

print(list[row][column])