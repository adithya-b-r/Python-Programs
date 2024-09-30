def get_data():
    user_name = input("Enter your name : ")
    user_age = int(input("Enter your age : "))
    data_tuple = (user_name,user_age)
    return data_tuple

def message(username,userage):
    if userage <= 10:
        print("Hello",username)
    else :
        print("Hi,",username)

def main():
    user_name,user_age = get_data()
    message(user_name,user_age)

main()