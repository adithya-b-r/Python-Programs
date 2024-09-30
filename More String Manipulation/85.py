vowels = ['a','e','i','o','u']
count=0
name = input("Enter your name : ")
name = name.lower()

for i in name:
    for j in vowels:
        if i == j:
            count=count+1

print("There are",count,"vowels in your name!")