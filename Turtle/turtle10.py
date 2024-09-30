import turtle as t
import random as r

t.pensize(3)
scr = t.Screen()
scr.bgcolor("black")
for i in range(0,10):
    t.color(r.choice(["red","green","blue","yellow","pink","orange"]))
    for j in range(0,8):
        t.forward(100)
        t.right(45)
    t.right(36)

t.hideturtle()

t.exitonclick()