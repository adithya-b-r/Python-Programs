check = True

word = input("Enter a word in uppercase : ")

while word.isupper() != True:
    word = input("Try again : ")

print(word)