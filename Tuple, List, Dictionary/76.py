names = []

invite = True

for i in range(0,3):
    names.append(input("Enter a name of a person to invite for party : "))

while invite == True:
    more = input("Do you want to invite more peoples [y/n] : ")
    if more == 'n':
        invite = False
    else:
        names.append(input("Enter a name of a person to invite for party : "))

print(len(names),"people are arriving for party!")