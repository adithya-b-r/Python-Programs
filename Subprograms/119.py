from random import randint

def pick():
    low = int(input("Enter low number : "))
    high = int(input("Enter high number : "))
    return (low,high)

def ran(x,y):
    num = randint(x,y)
    return num

def guess():
    unum = int(input("I am thinking of a number... : "))
    return unum

def check(cn,un):
    if cn == un:
        print("Correct, you win!")
    else:
        if cn > un:
            print("Too low!")
        else:
            print("Too high!")
        un = guess()
        check(cn,un)

def main():
    num1, num2 = pick()
    comp_num = ran(num1, num2)
    unum = guess()
    check(comp_num,unum)

main()