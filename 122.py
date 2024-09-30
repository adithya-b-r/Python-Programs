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
    
def main():
    print("1) Add to file\n2) View all records\n3) Quit program")
    select = int(input("Enter the number of your selection : "))

    if select == 1:
        Add()
    elif select == 2:
        View()
    elif select == 3:
        print("Exiting...")
    else:
        print("Invalid selection!")

main()