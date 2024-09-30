print("[1] Create a new file")
print("[2] Display the file")
print("[3] Add a new item to the file\n")

sel = int(input("Make a selection (1, 2 or 3) : "))

if sel == 1:
    file = open("Subjects.txt","w")
    file.write(input("Enter a subject : "))
    file.close()

elif sel == 2:
    file = open("Subjects.txt","r")
    print(file.read())
    file.close()
    
elif sel == 3:
    file = open("Subjects.txt","a")
    file.write("\n"+input("Enter a new subject : "))
    file.close()

else:
    print("Wrong selection!")