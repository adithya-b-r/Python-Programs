foods = {}

for i in range(1,5):
    add = input("Enter your favorite food : ")
    foods[i] = add

print(foods)
del foods[int(input("Enter a food name to remove : "))]

print(foods)