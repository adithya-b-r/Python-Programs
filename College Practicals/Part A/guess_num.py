import random

class GNE(Exception):
    pass
class GH(GNE):
    pass
class GL(GNE):
    pass

def guess_number(stored_number):
    while True:
        try:
            guess = int(input("Guess the number : "))
            if guess == stored_number:
                print("Congratulations! You guessed the number!")
                break
            elif guess > stored_number:
                raise GH("Too High.")
            else:
                raise GL("Too Low.")
        except GH as e:
            print(e)
        except GL as e:
            print(e)
        except ValueError:
            print("Invalid input! Please try an integer!")

stored_number = random.randint(1,100)
guess_number(stored_number)