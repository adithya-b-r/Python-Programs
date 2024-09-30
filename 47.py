total=0
num1=int(input("Enter a number : "))
op="y"

while  op == "y":
    num2=int(input("Enter another number : "))
    total=num1+num2
    op=input("Do you want to add another number? [y/n] : ")
print("Total is",total)