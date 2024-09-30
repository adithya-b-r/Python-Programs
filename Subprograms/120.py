from random import randint

def add():
    n1 = randint(5,20)
    n2 = randint(5,20)
    cans = n1+n2
    uans = int(input(str(n1)+" + "+str(n2)+" = "))
    return (cans,uans)

def sub():
    n1 = randint(25,50)
    n2 = randint(1,25)
    cans = n1-n2
    uans = int(input(str(n1)+" - "+str(n2)+" = "))
    return (cans,uans)

def check(x,y):
    if x == y:
        print("Correct!")
    else:
        print("Incorrect, the answer is",str(x)+"!")

def main():
    print("[1] Addition \n[2] Subtraction")
    sel = int(input("Enter 1 or 2 : "))

    if sel == 1:
        cans,uans = add()
        check(cans,uans)
    elif sel == 2:
        cans,uans = sub()
        check(cans,uans)
    else:
        print("Invalid selection!")

main()