from distutils.command.clean import clean
from turtle import clearscreen


names = []

def add():
    newName = input("Enter new name : ")
    names.append(newName)
    main()

def change():
    row_num = 1
    for name in names:
        print(str(row_num)+".",name)
        row_num = row_num + 1

    ch = int(input("Enter a row number to change name : "))
    ch = ch - 1
    new_Name = input("Enter new name : ")
    names[ch] = new_Name
    main()

def delete():
    row_num = 1
    for name in names:
        print(str(row_num)+".",name)
        row_num = row_num + 1

    del_name = int(input("Enter a row number to delete name : "))
    del_name = del_name - 1
    del names[del_name]
    main()

def view():
    row_num = 1
    for name in names:
        print(str(row_num)+".",name)
        row_num = row_num + 1
    main()

def main():
    print("\n[1] Add a name \n[2] Change a name \n[3] Delete a name \n[4] View all the names \n[5] Exit \n")
    sel = int(input("Enter the number of your selection : "))

    if sel == 1:
        add()
    elif sel == 2:
        change()
    elif sel == 3:
        delete()
    elif sel == 4:
        view()
    elif sel == 5:
        print("Thank you, have a good day :)")
    else:
        print("Invalid selection!")
        main()

main()