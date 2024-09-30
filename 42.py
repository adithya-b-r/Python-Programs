total=0

for i in range (0,5):
    num=int(input("Enter a number : "))
    op=input("Do you want to include [y/n] : ")
    op=op.lower()
    if op == "y":
        total=total+num

print("Total =",total)