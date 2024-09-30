from typing import ChainMap


simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

row = int(input("Row : "))

print(simple_array[row])

column = int(input("Column : "))
print(simple_array[row][column])

change = input("Do you want to change the above value [y/n] : ")

if change == 'y':
    newValue = int(input("Enter new value : "))
    simple_array[row][column] = newValue

#simple_array[row].append(int(input("Enter a new value : ")))

print(simple_array[row])