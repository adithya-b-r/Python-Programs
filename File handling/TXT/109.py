print("1) Create a new file\n2) Display the file\n3) Add a new item to the file")

select=int(input("Make a selection : "))

if select == 1:
    file = open("Subjects.txt","w")
    subject=input("Enter a school subject : ")
    file.write(subject)
    file.close()

elif select == 2:
    file = open("Subjects.txt","r")
    print(file.read())
    file.close()

elif select == 3:
    file = open("Subjects.txt","a")
    subject=input("Enter a new subject : ")
    subject="\n"+subject
    file.write(subject)
    file.close()

    file = open("Subjects.txt","r")
    print(file.read())
    file.close()
    
else:
    print("Invalid selection!")