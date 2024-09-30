num=0

while num<10 or num>20 :
    num=int(input("Enter a number between [10-20] : "))
    if num < 10 :
        print("Too low!")
    else:
        if num > 20 :
            print("Too high!")
    print("Try again!")

print("Thank you!")