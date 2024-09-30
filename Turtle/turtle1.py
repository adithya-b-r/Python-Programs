'''Reference :
https://docs.micropython.org/en/latest/library/os.html
'''

import os

#list directories
print(os.listdir())

#Rename a file
#print(os.rename("first.txt","first_rn.txt"))
#print(os.rename("first_rn.txt","first.txt"))

#Return a tuple
print(os.uname())
#print(os.stat('/'))

print(os.sync())