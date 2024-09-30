import csv

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

def del_rec():
    tmp = []
    file = open("Salaries.csv","r")

    n = 1
    for row in file:
        print(str(n)+".",row)
        tmp.append(row)
        n = n + 1
    file.close()

    getrid = int(input("Enter a row number to delete record : "))
    getrid = getrid - 1
    del tmp[getrid]

    file = open("Salaries.csv","w")
    n = 1
    for row in tmp:
        print(str(n)+".",row)
        file.write(row)
        n = n + 1
    file.close()
    main()

def main():
    print("\n[1] Add to file \n[2] View all records \n[3] Delete a record \n[4] Quit program")
    sel = int(input("Enter the number of your selection : "))

    if sel == 1:
        add()
    elif sel == 2:
        view()
    elif sel == 3:
        del_rec()
    elif sel == 4:
        print("Exiting...")
        print("Thank you, have a good day!")
    else:
        print("Invalid selection!")

main()