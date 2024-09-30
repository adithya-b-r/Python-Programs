people = {}

for i in range(0,4):
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    shoe_size = int(input("Enter shoe size : "))

    people[name] = {"Age":age,"Shoe size":shoe_size}

print(people)
name = input("Enter a name to display details : ")
print(people[name])