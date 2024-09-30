count=0
op="y"

while op=="y":
    name=input("Enter the name of a person to invite for party : ")
    print(name,"has invited to the party!")
    count=count+1

    op=input("Do you want to invite anybody else? [y/n] : ")
print(count,"peoples are coming for party!")
