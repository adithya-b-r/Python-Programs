import turtle as t
import random as r

lines = r.randrange(5,20)

for i in range(0,lines):
    length = r.randrange(25,100)
    rotate = r.randrange(1,360, 5)
    t.forward(length)
    t.right(rotate)

t.exitonclick()