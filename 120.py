import random

def add():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    ans = num1+num2
    print(num1," + ",num2)
    uans = int(input("==> "))
    check(ans,uans)

def sub():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    ans = num1-num2
    print(num1," - ",num2)
    uans = int(input("==> "))
    check(ans,uans)

def check(ans,uans):
    if ans == uans:
        print("Correct!")
    else:
        print("Wrong, the correct answer is",ans)

def main():
    print("1) Addition \n2) Subtraction")
    select = int(input("Enter 1 or 2 : "))

    if select == 1:
        add()
    elif select == 2:
        sub()
    else:
        print("Invalid selection!")

main()