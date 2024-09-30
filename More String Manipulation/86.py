password = input("Enter a password : ")
a_pass = input("Enter it again : ")

if password == a_pass:
    print("Thank you!")
elif password.lower() == a_pass.lower():
    print("They must be in same case!")
else:
    print("Incorrect!")