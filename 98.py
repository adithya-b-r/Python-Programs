list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

row=int(input("Enter a row : "))

print(list[row])

num=int(input("Enter a value : "))

list[row].append(num)
print(list[row])