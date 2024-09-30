dir=input("Which direction to count [up/down] : ")
dir=dir.lower()

if dir == "up":
    num=int(input("Enter a number : "))
    for i in range (1,num+1):
        print(i)
elif dir == "down":
    num=int(input("Enter a number below 20 : "))
    if num <= 20:
        for i in range (20,num-1,-1):
            print(i)
    else:
        print("Too high!")
else:
    print("I don't understand!")