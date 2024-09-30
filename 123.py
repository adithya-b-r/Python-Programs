import csv

def Add():
    file = open("Salaries.csv","a")
    name = input("Enter name : ")
    salary = input("Enter salary : ")
    newRecord = name+", "+salary+"\n"
    file.write(newRecord)
    file.close()
    main()

def View():
    file = open("Salaries.csv","r")
    print(file.read())
    file.close()
    main()

def Delete():
    name_list = []
    file = open("Salaries.csv","r")

    for row in file:
        name_list.append(row)
    file.close()

    x = 0
    for row in name_list:
        print(x,row)
        x = x+1
    rm = int(input("Enter the row number to delete : "))
    del name_list[rm]

    file = open("Salaries.csv","w")
    for row in name_list:
        file.write(row)
    file.close()
    main()

def main():
    print("1) Add to file\n2) View all records\n3) Delete a record\n4) Quit program")
    select = int(input("Enter the number of your selection : "))

    if select == 1:
        Add()
    elif select == 2:
        View()
    elif select == 3:
        Delete()
    elif select == 4:
        print("Exiting...")
    else:
        print("Invalid selection!")
        main()

main()