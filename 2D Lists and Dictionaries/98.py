simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

row = int(input("Row : "))

print(simple_array[row])

simple_array[row].append(int(input("Enter a new value : ")))

print(simple_array[row])