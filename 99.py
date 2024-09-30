list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

row=int(input("Enter a row : "))

print(list[row])

column=int(input("Enter a column : "))

print(list[row][column])

change=input("Do you want to change the value [y/n] : ")

if change=="y":
    num=int(input("Enter a new value : "))
    list[row][column]=num

print(list[row])