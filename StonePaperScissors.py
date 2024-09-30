import random

def game(compchoice, userchoice): 
    if userchoice == compchoice:
       print("Draw!")
    elif userchoice == "rock":
        if compchoice == "paper":
            print("You lose!")
        else:
            print("you win")
    elif userchoice == "paper":
        if compchoice == "scissor":
            print("You lose!")
        else:
            print("you win")
    elif userchoice == "scissor":
        if compchoice == "rock":
            print("You lose!")
        else:
            print("you win")

    main()


def main():
    compchoice = random.choice(["rock","paper","scissor"])

    userchoice = int(input("Rock - 1, paper - 2, scissor - 3, exit - 0 : "))

    if userchoice == 1:
        userchoice = "rock"
    elif userchoice == 2:
        userchoice = "paper"
    elif userchoice == 3:
        userchoice = "scissor"
    elif userchoice == 0:
        exit()
    else:
        print("Invalid Selection!")

    game(compchoice,userchoice)

main()