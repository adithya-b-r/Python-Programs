import random

def pick_num():
    low = int(input("Pick a low number : "))
    high = int(input("Pick a high number : "))
    comp_num = random.randint(low,high)
    return comp_num

def first_guess():
    print("I am thinking of a number....")
    guess = int(input("What am I thinking of : "))
    return guess

def check_ans(comp_num,guess):
    tryagain = "true"
    while tryagain == "true":
        if comp_num == guess:
            tryagain = "false"
            print("Correct, you win!")
        elif comp_num > guess:
            guess = int(input("Too low, try again : "))
        else :
            guess = int(input("Too high, try again : "))

def main():
    comp_num = pick_num()
    guess = first_guess()
    check_ans(comp_num,guess)

main()