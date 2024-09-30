compnum=50
num=0
count=0

while num!= compnum:
    num=int(input("Enter a number : "))
    count=count+1

    if num < 50:
        print("Too low!")
    else:
        print("Too high!")

print("Well done, you took",count,"attempts!")
