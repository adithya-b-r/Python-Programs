def getnum():
    num = int(input("Enter a number : "))
    return num

def countnum(num):
    for i in range(1,num+1):
        print(i)

def main():
    num = getnum()
    countnum(num)

main()