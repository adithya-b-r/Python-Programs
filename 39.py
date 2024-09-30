num=int(input("Enter a number between [1-12] : "))

if num <= 12:
    for i in range (1,11):
        mul=num*i
        print(num,"x",i,"=",mul)
else:
    print("Entered number is greater than 12")