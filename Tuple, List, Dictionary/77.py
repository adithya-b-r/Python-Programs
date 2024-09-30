names = []

for i in range(0,3):
    names.append(input("Enter a name of a person to invite for party : "))

print(names)

getrid = input("Enter a name from list : ")

print(names.index(getrid))

per = input("Do you still want "+getrid+" to come for party? [y/n] : ")
if per == 'n':
    names.remove(getrid)

print(names)