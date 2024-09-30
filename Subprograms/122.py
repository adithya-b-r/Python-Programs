def add():
    file = open("Salaries.csv","a")
    name = input("Enter name : ")
    salary = int(input("Enter salary : "))
    record = name+", "+str(salary)+"\n"
    file.write(record)
    file.close()
    main()

def view():
    file = open("Salaries.csv","r")
    
    print(file.read())
    main()

def main():
    print("\n[1] Add to file \n[2] View all records \n[3] Quit program")
    sel = int(input("Enter the number of your selection : "))

    if sel == 1:
        add()
    elif sel == 2:
        view()
    elif sel == 3:
        print("Exiting...")
        print("Thank you, have a good day!")
    else:
        print("Invalid selection!")

main()