name_list=[]

def add_name():
    name_list.append(input("Enter a name : "))
    main()

def change_name():
    old_name = input("Enter previous name : ")
    new_name = input("Enter new name : ")
    index_num = name_list.index(old_name)
    name_list[index_num] = new_name
    main()

def delete_name():
    rm = input("Enter a name to remove : ")
    name_list.remove(rm)
    main()

def view_names():
    for name in name_list:
        print(name)
    main()

def main():
    print("1) Add name\n2) Change name\n3) Delete name\n4) View names\n5) Exit")
    select = int(input("Enter your selection : "))

    if select == 1:
        add_name()
    elif select == 2:
        change_name()
    elif select == 3:
        delete_name()
    elif select == 4:
        view_names()
    elif select == 5:
        print("Exiting...")
    else:
        print("Ivalid option!")
        main()

main()