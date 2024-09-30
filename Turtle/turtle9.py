import turtle as t
import random as r

t.pensize(3)
scr = t.Screen()
scr.bgcolor("black")
for i in range(0,8):
    t.color(r.choice(["red","green","blue","yellow","pink","orange"]))
    t.forward(100)
    t.left(45)

t.exitonclick()