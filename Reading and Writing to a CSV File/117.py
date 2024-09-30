import csv
from random import randint

name = input("Enter your name : ")
score = 0

num1 = randint(1,25)
num2 = randint(1,25)

q1 = str(num1)+" + "+str(num2)+" = "
q2 = str(num1)+" - "+str(num2)+" = "

uans1 = int(input(q1))
uans2 = int(input(q2))

sum = num1 + num2
diff = num1 - num2

if uans1 == sum:
    score = score + 1
if uans2 == diff:
    score = score + 1

file = open("MathsQuiz.csv","a")
record = "Name : "+name+", "+"Q1 : "+q1+str(uans1)+", "+"Q2 : "+q2+str(uans2)+", "+"Score : "+str(score)+"\n"
file.write(record)
file.close()