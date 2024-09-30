#Abandoned :(
import turtle as t

t.pensize(6)
t.penup()
t.right(180)
t.forward(300)
t.left(90)
t.forward(100)
t.left(180)
t.pendown()
t.pencolor("red")
for i in range(0,180):
    t.forward(6)
    t.right(2)

t.right(90)
t.forward(50)
t.right(90)


t.pencolor("orange")
for i in range(0,180):
    t.forward(6)
    t.left(2)

t.exitonclick()