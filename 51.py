num=10
bottle=0

while num!=bottle :
    print(num,"green bottles hanging on the wall, \nand if 1 green bottle should accidentally fall\n")
    num=num-1
    bottle=int(input("How many green bottles will be hanging on the wall? "))
    
    if num==0:
        print("\nThere are no more green bottles hanging on the wall :(")
        exit()
    else:
        if num != bottle:
            print("No, try again!\n")

print("\nThere will be",num,"bottles hanging on the wall!")