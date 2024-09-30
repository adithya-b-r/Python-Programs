name=input("Enter your name : ")
num=int(input("Enter a number [1-10] : "))

if num <= 10:
    for i in range (0,num):
        print(name)
else :
    for i in range (0,3):
        print("Too high!")