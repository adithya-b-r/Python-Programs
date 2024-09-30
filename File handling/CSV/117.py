import csv
import random

score = 0

name = input("Enter your name : ")
num1 = random.randint(1,50)
num2 = random.randint(1,50)
add=num1+num2

question1 = str(num1)+" + "+str(num2)+" = "
ans1=int(input(question1))

if ans1 == add:
    score=score+1

num1 = random.randint(1,50)
num2 = random.randint(1,50)
add=num1+num2

question2 = str(num1)+" + "+str(num2)+" = "
ans2=int(input(question2))

if ans2 == add:
    score=score+1

file = open("math_quiz.csv","a")
record = name+", "+"Q1 : "+question1+", "+str(ans1)+", "+"Q2 : "+question2+", "+str(ans2)+", "+str(score)+"\n"
file.write(record)

file.close()