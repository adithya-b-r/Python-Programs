subjects = ["English","Kannada","Hindi","Science","Maths","Social Science"]

print(subjects)

getrid = input("Enter a subject to remove : ")
getrid = subjects.index(getrid)
del subjects[getrid]
print(subjects)